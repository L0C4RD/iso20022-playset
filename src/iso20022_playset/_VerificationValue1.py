# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime
from . import ISOTime
from . import Max2048Text
from . import Max35Text
from . import Max5000Binary
from . import Max9999HexBinaryText

class VerificationValue1(base_types._BaseFieldType):

	__slots__ = ["_BinryVal", "_DtTm", "_HexBinryVal", "_Nm", "_TxtVal", "_VldtyEndDt", "_VldtyEndTm"]
	@property
	def BinryVal(self):
		return self._BinryVal

	@BinryVal.setter
	def BinryVal(self, value):
		self._BinryVal = value if value is not None else base_types.UninitialisedField(self, 'BinryVal', Max5000Binary, False)

	@BinryVal.deleter
	def BinryVal(self):
		del self._BinryVal
		self._BinryVal = base_types.UninitialisedField(self, 'BinryVal', Max5000Binary, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def HexBinryVal(self):
		return self._HexBinryVal

	@HexBinryVal.setter
	def HexBinryVal(self, value):
		self._HexBinryVal = value if value is not None else base_types.UninitialisedField(self, 'HexBinryVal', Max9999HexBinaryText, False)

	@HexBinryVal.deleter
	def HexBinryVal(self):
		del self._HexBinryVal
		self._HexBinryVal = base_types.UninitialisedField(self, 'HexBinryVal', Max9999HexBinaryText, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def TxtVal(self):
		return self._TxtVal

	@TxtVal.setter
	def TxtVal(self, value):
		self._TxtVal = value if value is not None else base_types.UninitialisedField(self, 'TxtVal', Max2048Text, False)

	@TxtVal.deleter
	def TxtVal(self):
		del self._TxtVal
		self._TxtVal = base_types.UninitialisedField(self, 'TxtVal', Max2048Text, False)

	@property
	def VldtyEndDt(self):
		return self._VldtyEndDt

	@VldtyEndDt.setter
	def VldtyEndDt(self, value):
		self._VldtyEndDt = value if value is not None else base_types.UninitialisedField(self, 'VldtyEndDt', ISODate, False)

	@VldtyEndDt.deleter
	def VldtyEndDt(self):
		del self._VldtyEndDt
		self._VldtyEndDt = base_types.UninitialisedField(self, 'VldtyEndDt', ISODate, False)

	@property
	def VldtyEndTm(self):
		return self._VldtyEndTm

	@VldtyEndTm.setter
	def VldtyEndTm(self, value):
		self._VldtyEndTm = value if value is not None else base_types.UninitialisedField(self, 'VldtyEndTm', ISOTime, False)

	@VldtyEndTm.deleter
	def VldtyEndTm(self):
		del self._VldtyEndTm
		self._VldtyEndTm = base_types.UninitialisedField(self, 'VldtyEndTm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BinryVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HexBinryVal', type=Max9999HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxtVal', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyEndTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))