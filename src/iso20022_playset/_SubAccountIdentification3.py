# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationFormatChoice
from . import AggregateBalanceInformation3
from . import YesNoIndicator

class SubAccountIdentification3(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_BalForSubAcct", "_FngbInd", "_Id"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def BalForSubAcct(self):
		return self._BalForSubAcct

	@BalForSubAcct.setter
	def BalForSubAcct(self, value):
		self._BalForSubAcct = value if value is not None else base_types.UninitialisedField(self, 'BalForSubAcct', AggregateBalanceInformation3, True)

	@BalForSubAcct.deleter
	def BalForSubAcct(self):
		del self._BalForSubAcct
		self._BalForSubAcct = base_types.UninitialisedField(self, 'BalForSubAcct', AggregateBalanceInformation3, True)

	@property
	def FngbInd(self):
		return self._FngbInd

	@FngbInd.setter
	def FngbInd(self, value):
		self._FngbInd = value if value is not None else base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@FngbInd.deleter
	def FngbInd(self):
		del self._FngbInd
		self._FngbInd = base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForSubAcct', type=AggregateBalanceInformation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FngbInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentificationFormatChoice, min=1, max=1, mutex_group=None, array=False),
	))