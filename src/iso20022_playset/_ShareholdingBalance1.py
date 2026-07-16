# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat57Choice
from . import FinancialInstrumentQuantity18Choice
from . import PartyIdentification218
from . import ShareholdingType1Code
from . import SupplementaryData1

class ShareholdingBalance1(base_types._BaseFieldType):

	__slots__ = ["_InitlDtOfShrhldg", "_Qty", "_ShrhldgTp", "_SplmtryData", "_ThrdPty"]
	@property
	def InitlDtOfShrhldg(self):
		return self._InitlDtOfShrhldg

	@InitlDtOfShrhldg.setter
	def InitlDtOfShrhldg(self, value):
		self._InitlDtOfShrhldg = value if value is not None else base_types.UninitialisedField(self, 'InitlDtOfShrhldg', DateFormat57Choice, False)

	@InitlDtOfShrhldg.deleter
	def InitlDtOfShrhldg(self):
		del self._InitlDtOfShrhldg
		self._InitlDtOfShrhldg = base_types.UninitialisedField(self, 'InitlDtOfShrhldg', DateFormat57Choice, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity18Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity18Choice, False)

	@property
	def ShrhldgTp(self):
		return self._ShrhldgTp

	@ShrhldgTp.setter
	def ShrhldgTp(self, value):
		self._ShrhldgTp = value if value is not None else base_types.UninitialisedField(self, 'ShrhldgTp', ShareholdingType1Code, False)

	@ShrhldgTp.deleter
	def ShrhldgTp(self):
		del self._ShrhldgTp
		self._ShrhldgTp = base_types.UninitialisedField(self, 'ShrhldgTp', ShareholdingType1Code, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def ThrdPty(self):
		return self._ThrdPty

	@ThrdPty.setter
	def ThrdPty(self, value):
		self._ThrdPty = value if value is not None else base_types.UninitialisedField(self, 'ThrdPty', PartyIdentification218, True)

	@ThrdPty.deleter
	def ThrdPty(self):
		del self._ThrdPty
		self._ThrdPty = base_types.UninitialisedField(self, 'ThrdPty', PartyIdentification218, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlDtOfShrhldg', type=DateFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgTp', type=ShareholdingType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ThrdPty', type=PartyIdentification218, min=0, max=None, mutex_group=None, array=True),
	))