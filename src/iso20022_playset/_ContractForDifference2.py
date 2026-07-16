# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import UnderlyingContractForDifferenceType3Code

class ContractForDifference2(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy1", "_NtnlCcy2", "_UndrlygTp"]
	@property
	def NtnlCcy1(self):
		return self._NtnlCcy1

	@NtnlCcy1.setter
	def NtnlCcy1(self, value):
		self._NtnlCcy1 = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcy1', ActiveOrHistoricCurrencyCode, False)

	@NtnlCcy1.deleter
	def NtnlCcy1(self):
		del self._NtnlCcy1
		self._NtnlCcy1 = base_types.UninitialisedField(self, 'NtnlCcy1', ActiveOrHistoricCurrencyCode, False)

	@property
	def NtnlCcy2(self):
		return self._NtnlCcy2

	@NtnlCcy2.setter
	def NtnlCcy2(self, value):
		self._NtnlCcy2 = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcy2', ActiveOrHistoricCurrencyCode, False)

	@NtnlCcy2.deleter
	def NtnlCcy2(self):
		del self._NtnlCcy2
		self._NtnlCcy2 = base_types.UninitialisedField(self, 'NtnlCcy2', ActiveOrHistoricCurrencyCode, False)

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if value is not None else base_types.UninitialisedField(self, 'UndrlygTp', UnderlyingContractForDifferenceType3Code, False)

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = base_types.UninitialisedField(self, 'UndrlygTp', UnderlyingContractForDifferenceType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy1', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy2', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=UnderlyingContractForDifferenceType3Code, min=1, max=1, mutex_group=None, array=False),
	))