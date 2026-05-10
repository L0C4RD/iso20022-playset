import base_types
import FinancialInstrumentQuantity18Choice
import ShareholdingType1Code
import PartyIdentification218
import SupplementaryData1
import DateFormat57Choice

class ShareholdingBalance1(base_types._BaseFieldType):

	__slots__ = ["_InitlDtOfShrhldg", "_SplmtryData", "_Qty", "_ShrhldgTp", "_ThrdPty"]
	@property
	def InitlDtOfShrhldg(self):
		return self._InitlDtOfShrhldg

	@InitlDtOfShrhldg.setter
	def InitlDtOfShrhldg(self, value):
		self._InitlDtOfShrhldg = value if type(value) != auto else self.make_default("InitlDtOfShrhldg")

	@InitlDtOfShrhldg.deleter
	def InitlDtOfShrhldg(self):
		del self._InitlDtOfShrhldg
		self._InitlDtOfShrhldg = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def ShrhldgTp(self):
		return self._ShrhldgTp

	@ShrhldgTp.setter
	def ShrhldgTp(self, value):
		self._ShrhldgTp = value if type(value) != auto else self.make_default("ShrhldgTp")

	@ShrhldgTp.deleter
	def ShrhldgTp(self):
		del self._ShrhldgTp
		self._ShrhldgTp = None

	@property
	def ThrdPty(self):
		return self._ThrdPty

	@ThrdPty.setter
	def ThrdPty(self, value):
		self._ThrdPty = value if type(value) != auto else self.make_default("ThrdPty")

	@ThrdPty.deleter
	def ThrdPty(self):
		del self._ThrdPty
		self._ThrdPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlDtOfShrhldg', type=DateFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgTp', type=ShareholdingType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPty', type=PartyIdentification218, min=0, max=None, mutex_group=None, array=True),
	))

