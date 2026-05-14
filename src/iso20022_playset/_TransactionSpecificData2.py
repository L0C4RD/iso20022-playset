# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._FleetLineItem6 import FleetLineItem6
from ._Max16HexBinaryText import Max16HexBinaryText

class TransactionSpecificData2(base_types._BaseFieldType):

	__slots__ = ["_FleetLineItm", "_NtlData", "_PrvtData", "_PurchsRstrctn"]
	@property
	def FleetLineItm(self):
		return self._FleetLineItm

	@FleetLineItm.setter
	def FleetLineItm(self, value):
		self._FleetLineItm = value if type(value) != base_types.auto else self.make_default("FleetLineItm")

	@FleetLineItm.deleter
	def FleetLineItm(self):
		del self._FleetLineItm
		self._FleetLineItm = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def PurchsRstrctn(self):
		return self._PurchsRstrctn

	@PurchsRstrctn.setter
	def PurchsRstrctn(self, value):
		self._PurchsRstrctn = value if type(value) != base_types.auto else self.make_default("PurchsRstrctn")

	@PurchsRstrctn.deleter
	def PurchsRstrctn(self):
		del self._PurchsRstrctn
		self._PurchsRstrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FleetLineItm', type=FleetLineItem6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsRstrctn', type=Max16HexBinaryText, min=0, max=1, mutex_group=None, array=False),
	))