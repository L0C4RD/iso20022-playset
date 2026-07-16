# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BarcodeType1Code
from . import Max16Text
from . import Max3000Binary
from . import Max8000Text
from . import QRCodeEncodingMode1Code
from . import QRCodeErrorCorrection1Code

class OutputBarcode2(base_types._BaseFieldType):

	__slots__ = ["_BrcdTp", "_BrcdVal", "_QRCdBinryVal", "_QRCdErrCrrctn", "_QRCdNcodgMd", "_QRCdVrsn"]
	@property
	def BrcdTp(self):
		return self._BrcdTp

	@BrcdTp.setter
	def BrcdTp(self, value):
		self._BrcdTp = value if value is not None else base_types.UninitialisedField(self, 'BrcdTp', BarcodeType1Code, False)

	@BrcdTp.deleter
	def BrcdTp(self):
		del self._BrcdTp
		self._BrcdTp = base_types.UninitialisedField(self, 'BrcdTp', BarcodeType1Code, False)

	@property
	def BrcdVal(self):
		return self._BrcdVal

	@BrcdVal.setter
	def BrcdVal(self, value):
		self._BrcdVal = value if value is not None else base_types.UninitialisedField(self, 'BrcdVal', Max8000Text, False)

	@BrcdVal.deleter
	def BrcdVal(self):
		del self._BrcdVal
		self._BrcdVal = base_types.UninitialisedField(self, 'BrcdVal', Max8000Text, False)

	@property
	def QRCdBinryVal(self):
		return self._QRCdBinryVal

	@QRCdBinryVal.setter
	def QRCdBinryVal(self, value):
		self._QRCdBinryVal = value if value is not None else base_types.UninitialisedField(self, 'QRCdBinryVal', Max3000Binary, False)

	@QRCdBinryVal.deleter
	def QRCdBinryVal(self):
		del self._QRCdBinryVal
		self._QRCdBinryVal = base_types.UninitialisedField(self, 'QRCdBinryVal', Max3000Binary, False)

	@property
	def QRCdErrCrrctn(self):
		return self._QRCdErrCrrctn

	@QRCdErrCrrctn.setter
	def QRCdErrCrrctn(self, value):
		self._QRCdErrCrrctn = value if value is not None else base_types.UninitialisedField(self, 'QRCdErrCrrctn', QRCodeErrorCorrection1Code, False)

	@QRCdErrCrrctn.deleter
	def QRCdErrCrrctn(self):
		del self._QRCdErrCrrctn
		self._QRCdErrCrrctn = base_types.UninitialisedField(self, 'QRCdErrCrrctn', QRCodeErrorCorrection1Code, False)

	@property
	def QRCdNcodgMd(self):
		return self._QRCdNcodgMd

	@QRCdNcodgMd.setter
	def QRCdNcodgMd(self, value):
		self._QRCdNcodgMd = value if value is not None else base_types.UninitialisedField(self, 'QRCdNcodgMd', QRCodeEncodingMode1Code, False)

	@QRCdNcodgMd.deleter
	def QRCdNcodgMd(self):
		del self._QRCdNcodgMd
		self._QRCdNcodgMd = base_types.UninitialisedField(self, 'QRCdNcodgMd', QRCodeEncodingMode1Code, False)

	@property
	def QRCdVrsn(self):
		return self._QRCdVrsn

	@QRCdVrsn.setter
	def QRCdVrsn(self, value):
		self._QRCdVrsn = value if value is not None else base_types.UninitialisedField(self, 'QRCdVrsn', Max16Text, False)

	@QRCdVrsn.deleter
	def QRCdVrsn(self):
		del self._QRCdVrsn
		self._QRCdVrsn = base_types.UninitialisedField(self, 'QRCdVrsn', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrcdTp', type=BarcodeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrcdVal', type=Max8000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdBinryVal', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdErrCrrctn', type=QRCodeErrorCorrection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdNcodgMd', type=QRCodeEncodingMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdVrsn', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))