# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtorActivation6
from . import ElectronicInvoice1

class DebtorActivationAmendment6(base_types._BaseFieldType):

	__slots__ = ["_DbtrActvtn", "_ElctrncInvcData"]
	@property
	def DbtrActvtn(self):
		return self._DbtrActvtn

	@DbtrActvtn.setter
	def DbtrActvtn(self, value):
		self._DbtrActvtn = value if value is not None else base_types.UninitialisedField(self, 'DbtrActvtn', DebtorActivation6, False)

	@DbtrActvtn.deleter
	def DbtrActvtn(self):
		del self._DbtrActvtn
		self._DbtrActvtn = base_types.UninitialisedField(self, 'DbtrActvtn', DebtorActivation6, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtrActvtn', type=DebtorActivation6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncInvcData', type=ElectronicInvoice1, min=0, max=1, mutex_group=None, array=False),
	))