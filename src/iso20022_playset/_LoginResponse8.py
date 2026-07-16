# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import ISODateTime
from . import PointOfInteractionCapabilities9
from . import PointOfInteractionComponent18

class LoginResponse8(base_types._BaseFieldType):

	__slots__ = ["_OutptDisp", "_POICpblties", "_POIDtTm", "_POISftwr"]
	@property
	def OutptDisp(self):
		return self._OutptDisp

	@OutptDisp.setter
	def OutptDisp(self, value):
		self._OutptDisp = value if value is not None else base_types.UninitialisedField(self, 'OutptDisp', ActionMessage12, False)

	@OutptDisp.deleter
	def OutptDisp(self):
		del self._OutptDisp
		self._OutptDisp = base_types.UninitialisedField(self, 'OutptDisp', ActionMessage12, False)

	@property
	def POICpblties(self):
		return self._POICpblties

	@POICpblties.setter
	def POICpblties(self, value):
		self._POICpblties = value if value is not None else base_types.UninitialisedField(self, 'POICpblties', PointOfInteractionCapabilities9, False)

	@POICpblties.deleter
	def POICpblties(self):
		del self._POICpblties
		self._POICpblties = base_types.UninitialisedField(self, 'POICpblties', PointOfInteractionCapabilities9, False)

	@property
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if value is not None else base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

	@property
	def POISftwr(self):
		return self._POISftwr

	@POISftwr.setter
	def POISftwr(self, value):
		self._POISftwr = value if value is not None else base_types.UninitialisedField(self, 'POISftwr', PointOfInteractionComponent18, True)

	@POISftwr.deleter
	def POISftwr(self):
		del self._POISftwr
		self._POISftwr = base_types.UninitialisedField(self, 'POISftwr', PointOfInteractionComponent18, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutptDisp', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICpblties', type=PointOfInteractionCapabilities9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POISftwr', type=PointOfInteractionComponent18, min=1, max=None, mutex_group=None, array=True),
	))