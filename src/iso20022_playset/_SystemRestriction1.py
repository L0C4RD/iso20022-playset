# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text

class SystemRestriction1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_VldFr", "_VldTo"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if value is not None else base_types.UninitialisedField(self, 'VldTo', ISODateTime, False)

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = base_types.UninitialisedField(self, 'VldTo', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))