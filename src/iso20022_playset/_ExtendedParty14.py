# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extended350Code
from . import InvestmentAccountOwnershipInformation16

class ExtendedParty14(base_types._BaseFieldType):

	__slots__ = ["_OthrPtyDtls", "_XtndedPtyRole"]
	@property
	def OthrPtyDtls(self):
		return self._OthrPtyDtls

	@OthrPtyDtls.setter
	def OthrPtyDtls(self, value):
		self._OthrPtyDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrPtyDtls', InvestmentAccountOwnershipInformation16, False)

	@OthrPtyDtls.deleter
	def OthrPtyDtls(self):
		del self._OthrPtyDtls
		self._OthrPtyDtls = base_types.UninitialisedField(self, 'OthrPtyDtls', InvestmentAccountOwnershipInformation16, False)

	@property
	def XtndedPtyRole(self):
		return self._XtndedPtyRole

	@XtndedPtyRole.setter
	def XtndedPtyRole(self, value):
		self._XtndedPtyRole = value if value is not None else base_types.UninitialisedField(self, 'XtndedPtyRole', Extended350Code, False)

	@XtndedPtyRole.deleter
	def XtndedPtyRole(self):
		del self._XtndedPtyRole
		self._XtndedPtyRole = base_types.UninitialisedField(self, 'XtndedPtyRole', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPtyDtls', type=InvestmentAccountOwnershipInformation16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedPtyRole', type=Extended350Code, min=1, max=1, mutex_group=None, array=False),
	))