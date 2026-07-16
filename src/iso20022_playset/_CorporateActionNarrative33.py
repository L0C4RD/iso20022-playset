# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax350Text

class CorporateActionNarrative33(base_types._BaseFieldType):

	__slots__ = ["_DlvryDtls", "_FXInstrsAddtlInf", "_InfToCmplyWth", "_InstrAddtlInf"]
	@property
	def DlvryDtls(self):
		return self._DlvryDtls

	@DlvryDtls.setter
	def DlvryDtls(self, value):
		self._DlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'DlvryDtls', RestrictedFINXMax350Text, True)

	@DlvryDtls.deleter
	def DlvryDtls(self):
		del self._DlvryDtls
		self._DlvryDtls = base_types.UninitialisedField(self, 'DlvryDtls', RestrictedFINXMax350Text, True)

	@property
	def FXInstrsAddtlInf(self):
		return self._FXInstrsAddtlInf

	@FXInstrsAddtlInf.setter
	def FXInstrsAddtlInf(self, value):
		self._FXInstrsAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'FXInstrsAddtlInf', RestrictedFINXMax350Text, True)

	@FXInstrsAddtlInf.deleter
	def FXInstrsAddtlInf(self):
		del self._FXInstrsAddtlInf
		self._FXInstrsAddtlInf = base_types.UninitialisedField(self, 'FXInstrsAddtlInf', RestrictedFINXMax350Text, True)

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if value is not None else base_types.UninitialisedField(self, 'InfToCmplyWth', RestrictedFINXMax350Text, True)

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = base_types.UninitialisedField(self, 'InfToCmplyWth', RestrictedFINXMax350Text, True)

	@property
	def InstrAddtlInf(self):
		return self._InstrAddtlInf

	@InstrAddtlInf.setter
	def InstrAddtlInf(self, value):
		self._InstrAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'InstrAddtlInf', RestrictedFINXMax350Text, True)

	@InstrAddtlInf.deleter
	def InstrAddtlInf(self):
		del self._InstrAddtlInf
		self._InstrAddtlInf = base_types.UninitialisedField(self, 'InstrAddtlInf', RestrictedFINXMax350Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryDtls', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FXInstrsAddtlInf', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfToCmplyWth', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrAddtlInf', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
	))