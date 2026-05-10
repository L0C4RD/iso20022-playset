from . import base_types
from .Max5000Binary import Max5000Binary
from .Max35Text import Max35Text
from .Max9999HexBinaryText import Max9999HexBinaryText
from .ISOTime import ISOTime
from .ISODate import ISODate
from .Max2048Text import Max2048Text
from .ISODateTime import ISODateTime

class VerificationValue1(base_types._BaseFieldType):

	__slots__ = ["_DtTm", "_BinryVal", "_VldtyEndDt", "_TxtVal", "_Nm", "_HexBinryVal", "_VldtyEndTm"]
	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def BinryVal(self):
		return self._BinryVal

	@BinryVal.setter
	def BinryVal(self, value):
		self._BinryVal = value if type(value) != auto else self.make_default("BinryVal")

	@BinryVal.deleter
	def BinryVal(self):
		del self._BinryVal
		self._BinryVal = None

	@property
	def VldtyEndDt(self):
		return self._VldtyEndDt

	@VldtyEndDt.setter
	def VldtyEndDt(self, value):
		self._VldtyEndDt = value if type(value) != auto else self.make_default("VldtyEndDt")

	@VldtyEndDt.deleter
	def VldtyEndDt(self):
		del self._VldtyEndDt
		self._VldtyEndDt = None

	@property
	def TxtVal(self):
		return self._TxtVal

	@TxtVal.setter
	def TxtVal(self, value):
		self._TxtVal = value if type(value) != auto else self.make_default("TxtVal")

	@TxtVal.deleter
	def TxtVal(self):
		del self._TxtVal
		self._TxtVal = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def HexBinryVal(self):
		return self._HexBinryVal

	@HexBinryVal.setter
	def HexBinryVal(self, value):
		self._HexBinryVal = value if type(value) != auto else self.make_default("HexBinryVal")

	@HexBinryVal.deleter
	def HexBinryVal(self):
		del self._HexBinryVal
		self._HexBinryVal = None

	@property
	def VldtyEndTm(self):
		return self._VldtyEndTm

	@VldtyEndTm.setter
	def VldtyEndTm(self, value):
		self._VldtyEndTm = value if type(value) != auto else self.make_default("VldtyEndTm")

	@VldtyEndTm.deleter
	def VldtyEndTm(self):
		del self._VldtyEndTm
		self._VldtyEndTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BinryVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxtVal', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HexBinryVal', type=Max9999HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyEndTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))

