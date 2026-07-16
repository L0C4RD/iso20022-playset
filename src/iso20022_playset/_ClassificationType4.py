# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalLegalFramework1Code
from . import ExternalRegulatoryInformationType1Code

class ClassificationType4(base_types._BaseFieldType):

	__slots__ = ["_InfTp", "_LglFrmwk"]
	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if value is not None else base_types.UninitialisedField(self, 'InfTp', ExternalRegulatoryInformationType1Code, False)

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = base_types.UninitialisedField(self, 'InfTp', ExternalRegulatoryInformationType1Code, False)

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if value is not None else base_types.UninitialisedField(self, 'LglFrmwk', ExternalLegalFramework1Code, True)

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = base_types.UninitialisedField(self, 'LglFrmwk', ExternalLegalFramework1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfTp', type=ExternalRegulatoryInformationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=ExternalLegalFramework1Code, min=1, max=None, mutex_group=None, array=True),
	))