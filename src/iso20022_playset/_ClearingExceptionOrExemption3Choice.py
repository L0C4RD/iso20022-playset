# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingExceptionOrExemption2
from . import NoReasonCode

class ClearingExceptionOrExemption3Choice(base_types._BaseFieldType):

	__slots__ = ["_CtrPties", "_Rsn"]
	@property
	def CtrPties(self):
		return self._CtrPties

	@CtrPties.setter
	def CtrPties(self, value):
		self._CtrPties = value if value is not None else base_types.UninitialisedField(self, 'CtrPties', ClearingExceptionOrExemption2, False)

	@CtrPties.deleter
	def CtrPties(self):
		del self._CtrPties
		self._CtrPties = base_types.UninitialisedField(self, 'CtrPties', ClearingExceptionOrExemption2, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', NoReasonCode, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPties', type=ClearingExceptionOrExemption2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))