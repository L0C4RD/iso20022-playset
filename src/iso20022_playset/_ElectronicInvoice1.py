# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PresentmentType1Code

class ElectronicInvoice1(base_types._BaseFieldType):

	__slots__ = ["_PresntmntTp"]
	@property
	def PresntmntTp(self):
		return self._PresntmntTp

	@PresntmntTp.setter
	def PresntmntTp(self, value):
		self._PresntmntTp = value if value is not None else base_types.UninitialisedField(self, 'PresntmntTp', PresentmentType1Code, False)

	@PresntmntTp.deleter
	def PresntmntTp(self):
		del self._PresntmntTp
		self._PresntmntTp = base_types.UninitialisedField(self, 'PresntmntTp', PresentmentType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PresntmntTp', type=PresentmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))