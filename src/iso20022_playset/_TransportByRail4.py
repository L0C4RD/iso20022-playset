# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max35Text
from . import Max70Text

class TransportByRail4(base_types._BaseFieldType):

	__slots__ = ["_CrrierAgtCtry", "_CrrierAgtNm", "_PlcOfDlvry", "_PlcOfRct", "_RailCrrierCtry", "_RailCrrierNm"]
	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@property
	def PlcOfDlvry(self):
		return self._PlcOfDlvry

	@PlcOfDlvry.setter
	def PlcOfDlvry(self, value):
		self._PlcOfDlvry = value if value is not None else base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, False)

	@PlcOfDlvry.deleter
	def PlcOfDlvry(self):
		del self._PlcOfDlvry
		self._PlcOfDlvry = base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, False)

	@property
	def PlcOfRct(self):
		return self._PlcOfRct

	@PlcOfRct.setter
	def PlcOfRct(self, value):
		self._PlcOfRct = value if value is not None else base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, False)

	@PlcOfRct.deleter
	def PlcOfRct(self):
		del self._PlcOfRct
		self._PlcOfRct = base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, False)

	@property
	def RailCrrierCtry(self):
		return self._RailCrrierCtry

	@RailCrrierCtry.setter
	def RailCrrierCtry(self, value):
		self._RailCrrierCtry = value if value is not None else base_types.UninitialisedField(self, 'RailCrrierCtry', CountryCode, False)

	@RailCrrierCtry.deleter
	def RailCrrierCtry(self):
		del self._RailCrrierCtry
		self._RailCrrierCtry = base_types.UninitialisedField(self, 'RailCrrierCtry', CountryCode, False)

	@property
	def RailCrrierNm(self):
		return self._RailCrrierNm

	@RailCrrierNm.setter
	def RailCrrierNm(self, value):
		self._RailCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'RailCrrierNm', Max70Text, False)

	@RailCrrierNm.deleter
	def RailCrrierNm(self):
		del self._RailCrrierNm
		self._RailCrrierNm = base_types.UninitialisedField(self, 'RailCrrierNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RailCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RailCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))