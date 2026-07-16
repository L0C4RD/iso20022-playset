# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOTime

class SettlementTimeRequest2(base_types._BaseFieldType):

	__slots__ = ["_CLSTm", "_FrTm", "_RjctTm", "_TillTm"]
	@property
	def CLSTm(self):
		return self._CLSTm

	@CLSTm.setter
	def CLSTm(self, value):
		self._CLSTm = value if value is not None else base_types.UninitialisedField(self, 'CLSTm', ISOTime, False)

	@CLSTm.deleter
	def CLSTm(self):
		del self._CLSTm
		self._CLSTm = base_types.UninitialisedField(self, 'CLSTm', ISOTime, False)

	@property
	def FrTm(self):
		return self._FrTm

	@FrTm.setter
	def FrTm(self, value):
		self._FrTm = value if value is not None else base_types.UninitialisedField(self, 'FrTm', ISOTime, False)

	@FrTm.deleter
	def FrTm(self):
		del self._FrTm
		self._FrTm = base_types.UninitialisedField(self, 'FrTm', ISOTime, False)

	@property
	def RjctTm(self):
		return self._RjctTm

	@RjctTm.setter
	def RjctTm(self, value):
		self._RjctTm = value if value is not None else base_types.UninitialisedField(self, 'RjctTm', ISOTime, False)

	@RjctTm.deleter
	def RjctTm(self):
		del self._RjctTm
		self._RjctTm = base_types.UninitialisedField(self, 'RjctTm', ISOTime, False)

	@property
	def TillTm(self):
		return self._TillTm

	@TillTm.setter
	def TillTm(self, value):
		self._TillTm = value if value is not None else base_types.UninitialisedField(self, 'TillTm', ISOTime, False)

	@TillTm.deleter
	def TillTm(self):
		del self._TillTm
		self._TillTm = base_types.UninitialisedField(self, 'TillTm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CLSTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TillTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))