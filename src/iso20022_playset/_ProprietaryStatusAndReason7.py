# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification47
from . import ProprietaryReason5

class ProprietaryStatusAndReason7(base_types._BaseFieldType):

	__slots__ = ["_PrtryRsn", "_PrtrySts"]
	@property
	def PrtryRsn(self):
		return self._PrtryRsn

	@PrtryRsn.setter
	def PrtryRsn(self, value):
		self._PrtryRsn = value if value is not None else base_types.UninitialisedField(self, 'PrtryRsn', ProprietaryReason5, True)

	@PrtryRsn.deleter
	def PrtryRsn(self):
		del self._PrtryRsn
		self._PrtryRsn = base_types.UninitialisedField(self, 'PrtryRsn', ProprietaryReason5, True)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', GenericIdentification47, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', GenericIdentification47, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryRsn', type=ProprietaryReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtrySts', type=GenericIdentification47, min=1, max=1, mutex_group=None, array=False),
	))