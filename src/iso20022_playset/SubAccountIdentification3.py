from . import base_types
from .YesNoIndicator import YesNoIndicator
from .AggregateBalanceInformation3 import AggregateBalanceInformation3
from .AccountIdentificationFormatChoice import AccountIdentificationFormatChoice

class SubAccountIdentification3(base_types._BaseFieldType):

	__slots__ = ["_Id", "_FngbInd", "_ActvtyInd", "_BalForSubAcct"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def FngbInd(self):
		return self._FngbInd

	@FngbInd.setter
	def FngbInd(self, value):
		self._FngbInd = value if type(value) != auto else self.make_default("FngbInd")

	@FngbInd.deleter
	def FngbInd(self):
		del self._FngbInd
		self._FngbInd = None

	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def BalForSubAcct(self):
		return self._BalForSubAcct

	@BalForSubAcct.setter
	def BalForSubAcct(self, value):
		self._BalForSubAcct = value if type(value) != auto else self.make_default("BalForSubAcct")

	@BalForSubAcct.deleter
	def BalForSubAcct(self):
		del self._BalForSubAcct
		self._BalForSubAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AccountIdentificationFormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FngbInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForSubAcct', type=AggregateBalanceInformation3, min=0, max=None, mutex_group=None, array=True),
	))

