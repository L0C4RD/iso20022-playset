# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import FleetLineItem6
from . import Max16HexBinaryText

class TransactionSpecificData2(base_types._BaseFieldType):

	__slots__ = ["_FleetLineItm", "_NtlData", "_PrvtData", "_PurchsRstrctn"]
	@property
	def FleetLineItm(self):
		return self._FleetLineItm

	@FleetLineItm.setter
	def FleetLineItm(self, value):
		self._FleetLineItm = value if value is not None else base_types.UninitialisedField(self, 'FleetLineItm', FleetLineItem6, True)

	@FleetLineItm.deleter
	def FleetLineItm(self):
		del self._FleetLineItm
		self._FleetLineItm = base_types.UninitialisedField(self, 'FleetLineItm', FleetLineItem6, True)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def PurchsRstrctn(self):
		return self._PurchsRstrctn

	@PurchsRstrctn.setter
	def PurchsRstrctn(self, value):
		self._PurchsRstrctn = value if value is not None else base_types.UninitialisedField(self, 'PurchsRstrctn', Max16HexBinaryText, False)

	@PurchsRstrctn.deleter
	def PurchsRstrctn(self):
		del self._PurchsRstrctn
		self._PurchsRstrctn = base_types.UninitialisedField(self, 'PurchsRstrctn', Max16HexBinaryText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FleetLineItm', type=FleetLineItem6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsRstrctn', type=Max16HexBinaryText, min=0, max=1, mutex_group=None, array=False),
	))