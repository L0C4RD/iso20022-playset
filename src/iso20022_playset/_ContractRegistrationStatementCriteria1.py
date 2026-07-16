# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TrueFalseIndicator

class ContractRegistrationStatementCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AddtlSpprtgDocJrnl", "_RgltryRuleVldtn", "_SpprtgDocJrnl", "_TxJrnl"]
	@property
	def AddtlSpprtgDocJrnl(self):
		return self._AddtlSpprtgDocJrnl

	@AddtlSpprtgDocJrnl.setter
	def AddtlSpprtgDocJrnl(self, value):
		self._AddtlSpprtgDocJrnl = value if value is not None else base_types.UninitialisedField(self, 'AddtlSpprtgDocJrnl', TrueFalseIndicator, False)

	@AddtlSpprtgDocJrnl.deleter
	def AddtlSpprtgDocJrnl(self):
		del self._AddtlSpprtgDocJrnl
		self._AddtlSpprtgDocJrnl = base_types.UninitialisedField(self, 'AddtlSpprtgDocJrnl', TrueFalseIndicator, False)

	@property
	def RgltryRuleVldtn(self):
		return self._RgltryRuleVldtn

	@RgltryRuleVldtn.setter
	def RgltryRuleVldtn(self, value):
		self._RgltryRuleVldtn = value if value is not None else base_types.UninitialisedField(self, 'RgltryRuleVldtn', TrueFalseIndicator, False)

	@RgltryRuleVldtn.deleter
	def RgltryRuleVldtn(self):
		del self._RgltryRuleVldtn
		self._RgltryRuleVldtn = base_types.UninitialisedField(self, 'RgltryRuleVldtn', TrueFalseIndicator, False)

	@property
	def SpprtgDocJrnl(self):
		return self._SpprtgDocJrnl

	@SpprtgDocJrnl.setter
	def SpprtgDocJrnl(self, value):
		self._SpprtgDocJrnl = value if value is not None else base_types.UninitialisedField(self, 'SpprtgDocJrnl', TrueFalseIndicator, False)

	@SpprtgDocJrnl.deleter
	def SpprtgDocJrnl(self):
		del self._SpprtgDocJrnl
		self._SpprtgDocJrnl = base_types.UninitialisedField(self, 'SpprtgDocJrnl', TrueFalseIndicator, False)

	@property
	def TxJrnl(self):
		return self._TxJrnl

	@TxJrnl.setter
	def TxJrnl(self, value):
		self._TxJrnl = value if value is not None else base_types.UninitialisedField(self, 'TxJrnl', TrueFalseIndicator, False)

	@TxJrnl.deleter
	def TxJrnl(self):
		del self._TxJrnl
		self._TxJrnl = base_types.UninitialisedField(self, 'TxJrnl', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSpprtgDocJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRuleVldtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtgDocJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))