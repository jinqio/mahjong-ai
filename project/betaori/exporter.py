#
#
# class BetaoriDataExporter:
#
#     @staticmethod
#     def export_player(tenpai_player, player):
#         table = tenpai_player.table
#
#         added_seats = [tenpai_player.seat, player.seat]
#         another_players = []
#
#         for x in table.players:
#             if x.seat not in added_seats:
#                 another_players.append(x)
#                 added_seats.append(x.seat)
#
#         second_player = another_players[0]
#         third_player = another_players[1]
#
#         return {
#             'debug_tenpai_player_hand': tenpai_player.closed_hand,
#
#             'log_id': table.log_id,
#             'round_wind': table.round_wind,
#             'dora_indicators': table.dora_indicators,
#             'tenpai_player_waiting': tenpai_player.waiting,
#             'tenpai_player_discards': [x.to_json() for x in tenpai_player.discards],
#             'tenpai_player_melds': [x.to_json() for x in tenpai_player.melds],
#             'tenpai_player_wind': tenpai_player.player_wind,
#             'tenpai_player_in_riichi': tenpai_player.in_riichi,
#             'player_hand': player.closed_hand,
#             'player_discards': [x.to_json() for x in player.discards],
#             'player_melds': [x.to_json() for x in player.melds],
#             'second_player_discards': [x.to_json() for x in second_player.discards],
#             'second_player_melds': [x.to_json() for x in second_player.melds],
#             'thirds_player_discards': [x.to_json() for x in third_player.discards],
#             'third_player_melds': [x.to_json() for x in third_player.melds],
#         }


# -*- coding: utf-8 -*-
from base.utils.utils import encode_discards, encode_melds


class BetaoriCSVExporter(object):

    @staticmethod
    def header():
        return [
            'log_id',
            'round_wind',
            'dora_indicators',
            'tenpai_player_hand',
            'tenpai_player_waiting',
            'tenpai_player_discards',
            'tenpai_player_melds',
            'tenpai_player_wind',
            'tenpai_player_in_riichi',
            'player_hand',
            'player_discards',
            'player_melds',
            'second_player_discards',
            'second_player_melds',
            'third_player_discards',
            'third_player_melds',
        ]

    @staticmethod
    def export_player(tenpai_player, player):
        table = tenpai_player.table

        added_seats = [tenpai_player.seat, player.seat]
        another_players = []

        for x in table.players:
            if x.seat not in added_seats:
                another_players.append(x)
                added_seats.append(x.seat)

        second_player = another_players[0]
        third_player = another_players[1]

        tenpai_player_waiting = []
        for x in tenpai_player.waiting:
            tenpai_player_waiting.append('{};{}'.format(
                x['tile'],
                x['cost'] or 0,
            ))

        assert len(tenpai_player_waiting) > 0

        data = [
            table.log_id,
            table.round_wind,
            ','.join([str(x) for x in table.dora_indicators]),
            ','.join([str(x) for x in tenpai_player.closed_hand]),
            ','.join(tenpai_player_waiting),
            encode_discards(tenpai_player.discards),
            encode_melds(tenpai_player.melds),
            tenpai_player.player_wind,
            tenpai_player.in_riichi and 1 or 0,
            ','.join([str(x) for x in player.closed_hand]),
            encode_discards(player.discards),
            encode_melds(player.melds),
            encode_discards(second_player.discards),
            encode_melds(second_player.melds),
            encode_discards(third_player.discards),
            encode_melds(third_player.melds),
        ]

        return data

