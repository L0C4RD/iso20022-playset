import base_types
import InvestmentAccountOwnershipInformation17
import Extended350Code

class ExtendedParty15(base_types._BaseFieldType):

	__slots__ = ["_XtndedPtyRole", "_OthrPtyDtls"]
	@property
	def XtndedPtyRole(self):
		return self._XtndedPtyRole

	@XtndedPtyRole.setter
	def XtndedPtyRole(self, value):
		self._XtndedPtyRole = value if type(value) != auto else self.make_default("XtndedPtyRole")

	@XtndedPtyRole.deleter
	def XtndedPtyRole(self):
		del self._XtndedPtyRole
		self._XtndedPtyRole = None

	@property
	def OthrPtyDtls(self):
		return self._OthrPtyDtls

	@OthrPtyDtls.setter
	def OthrPtyDtls(self, value):
		self._OthrPtyDtls = value if type(value) != auto else self.make_default("OthrPtyDtls")

	@OthrPtyDtls.deleter
	def OthrPtyDtls(self):
		del self._OthrPtyDtls
		self._OthrPtyDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XtndedPtyRole', type=Extended350Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPtyDtls', type=InvestmentAccountOwnershipInformation17, min=1, max=1, mutex_group=None, array=False),
	))

