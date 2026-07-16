# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivationHeader3
from . import DebtorActivation5
from . import ElectronicInvoice1
from . import SupplementaryData1

class RequestToPayDebtorActivationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_DbtrActvtn", "_ElctrncInvcData", "_Hdr", "_SplmtryData"]
	@property
	def DbtrActvtn(self):
		return self._DbtrActvtn

	@DbtrActvtn.setter
	def DbtrActvtn(self, value):
		self._DbtrActvtn = value if value is not None else base_types.UninitialisedField(self, 'DbtrActvtn', DebtorActivation5, True)

	@DbtrActvtn.deleter
	def DbtrActvtn(self):
		del self._DbtrActvtn
		self._DbtrActvtn = base_types.UninitialisedField(self, 'DbtrActvtn', DebtorActivation5, True)

	@property
	def ElctrncInvcData(self):
		return self._ElctrncInvcData

	@ElctrncInvcData.setter
	def ElctrncInvcData(self, value):
		self._ElctrncInvcData = value if value is not None else base_types.UninitialisedField(self, 'ElctrncInvcData', ElectronicInvoice1, False)

	@ElctrncInvcData.deleter
	def ElctrncInvcData(self):
		del self._ElctrncInvcData
		self._ElctrncInvcData = base_types.UninitialisedField(self, 'ElctrncInvcData', ElectronicInvoice1, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtrActvtn', type=DebtorActivation5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ElctrncInvcData', type=ElectronicInvoice1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))