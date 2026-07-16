# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption2
from . import ISODateTime

class CorporateActionDeactivationInstruction1(base_types._BaseFieldType):

	__slots__ = ["_DeactvtnDtAndTm", "_OptnDtls"]
	@property
	def DeactvtnDtAndTm(self):
		return self._DeactvtnDtAndTm

	@DeactvtnDtAndTm.setter
	def DeactvtnDtAndTm(self, value):
		self._DeactvtnDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'DeactvtnDtAndTm', ISODateTime, False)

	@DeactvtnDtAndTm.deleter
	def DeactvtnDtAndTm(self):
		del self._DeactvtnDtAndTm
		self._DeactvtnDtAndTm = base_types.UninitialisedField(self, 'DeactvtnDtAndTm', ISODateTime, False)

	@property
	def OptnDtls(self):
		return self._OptnDtls

	@OptnDtls.setter
	def OptnDtls(self, value):
		self._OptnDtls = value if value is not None else base_types.UninitialisedField(self, 'OptnDtls', CorporateActionOption2, True)

	@OptnDtls.deleter
	def OptnDtls(self):
		del self._OptnDtls
		self._OptnDtls = base_types.UninitialisedField(self, 'OptnDtls', CorporateActionOption2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeactvtnDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnDtls', type=CorporateActionOption2, min=0, max=None, mutex_group=None, array=True),
	))