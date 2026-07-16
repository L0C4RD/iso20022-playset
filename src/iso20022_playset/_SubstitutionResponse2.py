# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralSubstitutionResponse1
from . import CollateralSubstitutionResponse3
from . import Status4Code

class SubstitutionResponse2(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnAccptncDtls", "_CollSbstitnRjctnDtls", "_RspnTp"]
	@property
	def CollSbstitnAccptncDtls(self):
		return self._CollSbstitnAccptncDtls

	@CollSbstitnAccptncDtls.setter
	def CollSbstitnAccptncDtls(self, value):
		self._CollSbstitnAccptncDtls = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnAccptncDtls', CollateralSubstitutionResponse1, False)

	@CollSbstitnAccptncDtls.deleter
	def CollSbstitnAccptncDtls(self):
		del self._CollSbstitnAccptncDtls
		self._CollSbstitnAccptncDtls = base_types.UninitialisedField(self, 'CollSbstitnAccptncDtls', CollateralSubstitutionResponse1, False)

	@property
	def CollSbstitnRjctnDtls(self):
		return self._CollSbstitnRjctnDtls

	@CollSbstitnRjctnDtls.setter
	def CollSbstitnRjctnDtls(self, value):
		self._CollSbstitnRjctnDtls = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRjctnDtls', CollateralSubstitutionResponse3, False)

	@CollSbstitnRjctnDtls.deleter
	def CollSbstitnRjctnDtls(self):
		del self._CollSbstitnRjctnDtls
		self._CollSbstitnRjctnDtls = base_types.UninitialisedField(self, 'CollSbstitnRjctnDtls', CollateralSubstitutionResponse3, False)

	@property
	def RspnTp(self):
		return self._RspnTp

	@RspnTp.setter
	def RspnTp(self, value):
		self._RspnTp = value if value is not None else base_types.UninitialisedField(self, 'RspnTp', Status4Code, False)

	@RspnTp.deleter
	def RspnTp(self):
		del self._RspnTp
		self._RspnTp = base_types.UninitialisedField(self, 'RspnTp', Status4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnAccptncDtls', type=CollateralSubstitutionResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRjctnDtls', type=CollateralSubstitutionResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
	))