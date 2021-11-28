# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Equipo(models.Model):
    _name = 'equipo'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    ciudad = fields.Char(string='Ciudad')
    fecha_fundacion = fields.Date(string='Fecha de Fundación')
    jugadores = fields.One2many('jugador', 'equipo_id', string='Jugadores')


class Jugador(models.Model):
    _name = 'jugador'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    posicion = fields.Selection([('portero', 'Portero'),
                                 ('extremo derecho', 'Extremo Derecho'),
                                 ('lateral derecho', 'Lateral Derecho'),
                                 ('central', 'Central'),
                                 ('lateral izquierda', 'Lateral Izquierdo'),
                                 ('extremo izquierdo', 'Extremo Izquierdo'),
                                 ('pivote', 'Pivote')],
                                string='Posición')
    equipo_id = fields.Many2one('equipo', string='Equipo')

