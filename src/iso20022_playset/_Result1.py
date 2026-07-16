# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max210Text

class Result1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DueToPtyA", "_DueToPtyB"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@property
	def DueToPtyA(self):
		return self._DueToPtyA

	@DueToPtyA.setter
	def DueToPtyA(self, value):
		self._DueToPtyA = value if value is not None else base_types.UninitialisedField(self, 'DueToPtyA', ActiveCurrencyAndAmount, False)

	@DueToPtyA.deleter
	def DueToPtyA(self):
		del self._DueToPtyA
		self._DueToPtyA = base_types.UninitialisedField(self, 'DueToPtyA', ActiveCurrencyAndAmount, False)

	@property
	def DueToPtyB(self):
		return self._DueToPtyB

	@DueToPtyB.setter
	def DueToPtyB(self, value):
		self._DueToPtyB = value if value is not None else base_types.UninitialisedField(self, 'DueToPtyB', ActiveCurrencyAndAmount, False)

	@DueToPtyB.deleter
	def DueToPtyB(self):
		del self._DueToPtyB
		self._DueToPtyB = base_types.UninitialisedField(self, 'DueToPtyB', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))