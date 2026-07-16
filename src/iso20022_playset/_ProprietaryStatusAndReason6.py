# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import ProprietaryReason4

class ProprietaryStatusAndReason6(base_types._BaseFieldType):

	__slots__ = ["_PrtryRsn", "_PrtrySts"]
	@property
	def PrtryRsn(self):
		return self._PrtryRsn

	@PrtryRsn.setter
	def PrtryRsn(self, value):
		self._PrtryRsn = value if value is not None else base_types.UninitialisedField(self, 'PrtryRsn', ProprietaryReason4, True)

	@PrtryRsn.deleter
	def PrtryRsn(self):
		del self._PrtryRsn
		self._PrtryRsn = base_types.UninitialisedField(self, 'PrtryRsn', ProprietaryReason4, True)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', GenericIdentification30, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryRsn', type=ProprietaryReason4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtrySts', type=GenericIdentification30, min=1, max=1, mutex_group=None, array=False),
	))