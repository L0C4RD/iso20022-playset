import base_types
import ExternalBankTransactionFamily1Code
import ExternalBankTransactionSubFamily1Code

class BankTransactionCodeStructure6(base_types._BaseFieldType):

	__slots__ = ["_SubFmlyCd", "_Cd"]
	@property
	def SubFmlyCd(self):
		return self._SubFmlyCd

	@SubFmlyCd.setter
	def SubFmlyCd(self, value):
		self._SubFmlyCd = value if type(value) != auto else self.make_default("SubFmlyCd")

	@SubFmlyCd.deleter
	def SubFmlyCd(self):
		del self._SubFmlyCd
		self._SubFmlyCd = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubFmlyCd', type=ExternalBankTransactionSubFamily1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=ExternalBankTransactionFamily1Code, min=1, max=1, mutex_group=None, array=False),
	))

