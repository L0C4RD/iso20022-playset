# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification175
from . import TrueFalseIndicator

class NonFinancialInstitutionSector10(base_types._BaseFieldType):

	__slots__ = ["_ClrThrshld", "_DrctlyLkdActvty", "_FdrlInstn", "_Sctr"]
	@property
	def ClrThrshld(self):
		return self._ClrThrshld

	@ClrThrshld.setter
	def ClrThrshld(self, value):
		self._ClrThrshld = value if value is not None else base_types.UninitialisedField(self, 'ClrThrshld', TrueFalseIndicator, False)

	@ClrThrshld.deleter
	def ClrThrshld(self):
		del self._ClrThrshld
		self._ClrThrshld = base_types.UninitialisedField(self, 'ClrThrshld', TrueFalseIndicator, False)

	@property
	def DrctlyLkdActvty(self):
		return self._DrctlyLkdActvty

	@DrctlyLkdActvty.setter
	def DrctlyLkdActvty(self, value):
		self._DrctlyLkdActvty = value if value is not None else base_types.UninitialisedField(self, 'DrctlyLkdActvty', TrueFalseIndicator, False)

	@DrctlyLkdActvty.deleter
	def DrctlyLkdActvty(self):
		del self._DrctlyLkdActvty
		self._DrctlyLkdActvty = base_types.UninitialisedField(self, 'DrctlyLkdActvty', TrueFalseIndicator, False)

	@property
	def FdrlInstn(self):
		return self._FdrlInstn

	@FdrlInstn.setter
	def FdrlInstn(self, value):
		self._FdrlInstn = value if value is not None else base_types.UninitialisedField(self, 'FdrlInstn', TrueFalseIndicator, False)

	@FdrlInstn.deleter
	def FdrlInstn(self):
		del self._FdrlInstn
		self._FdrlInstn = base_types.UninitialisedField(self, 'FdrlInstn', TrueFalseIndicator, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', GenericIdentification175, True)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', GenericIdentification175, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrThrshld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctlyLkdActvty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FdrlInstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=GenericIdentification175, min=1, max=None, mutex_group=None, array=True),
	))