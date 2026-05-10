from . import base_types
from .BarcodeType1Code import BarcodeType1Code
from .Max16Text import Max16Text
from .Max3000Binary import Max3000Binary
from .QRCodeErrorCorrection1Code import QRCodeErrorCorrection1Code
from .QRCodeEncodingMode1Code import QRCodeEncodingMode1Code
from .Max8000Text import Max8000Text

class OutputBarcode2(base_types._BaseFieldType):

	__slots__ = ["_BrcdVal", "_QRCdErrCrrctn", "_QRCdBinryVal", "_BrcdTp", "_QRCdNcodgMd", "_QRCdVrsn"]
	@property
	def BrcdVal(self):
		return self._BrcdVal

	@BrcdVal.setter
	def BrcdVal(self, value):
		self._BrcdVal = value if type(value) != auto else self.make_default("BrcdVal")

	@BrcdVal.deleter
	def BrcdVal(self):
		del self._BrcdVal
		self._BrcdVal = None

	@property
	def QRCdErrCrrctn(self):
		return self._QRCdErrCrrctn

	@QRCdErrCrrctn.setter
	def QRCdErrCrrctn(self, value):
		self._QRCdErrCrrctn = value if type(value) != auto else self.make_default("QRCdErrCrrctn")

	@QRCdErrCrrctn.deleter
	def QRCdErrCrrctn(self):
		del self._QRCdErrCrrctn
		self._QRCdErrCrrctn = None

	@property
	def QRCdBinryVal(self):
		return self._QRCdBinryVal

	@QRCdBinryVal.setter
	def QRCdBinryVal(self, value):
		self._QRCdBinryVal = value if type(value) != auto else self.make_default("QRCdBinryVal")

	@QRCdBinryVal.deleter
	def QRCdBinryVal(self):
		del self._QRCdBinryVal
		self._QRCdBinryVal = None

	@property
	def BrcdTp(self):
		return self._BrcdTp

	@BrcdTp.setter
	def BrcdTp(self, value):
		self._BrcdTp = value if type(value) != auto else self.make_default("BrcdTp")

	@BrcdTp.deleter
	def BrcdTp(self):
		del self._BrcdTp
		self._BrcdTp = None

	@property
	def QRCdNcodgMd(self):
		return self._QRCdNcodgMd

	@QRCdNcodgMd.setter
	def QRCdNcodgMd(self, value):
		self._QRCdNcodgMd = value if type(value) != auto else self.make_default("QRCdNcodgMd")

	@QRCdNcodgMd.deleter
	def QRCdNcodgMd(self):
		del self._QRCdNcodgMd
		self._QRCdNcodgMd = None

	@property
	def QRCdVrsn(self):
		return self._QRCdVrsn

	@QRCdVrsn.setter
	def QRCdVrsn(self, value):
		self._QRCdVrsn = value if type(value) != auto else self.make_default("QRCdVrsn")

	@QRCdVrsn.deleter
	def QRCdVrsn(self):
		del self._QRCdVrsn
		self._QRCdVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrcdVal', type=Max8000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdErrCrrctn', type=QRCodeErrorCorrection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdBinryVal', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrcdTp', type=BarcodeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdNcodgMd', type=QRCodeEncodingMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdVrsn', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))

