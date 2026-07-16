# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ProcessingPosition9Choice

class Linkages41(base_types._BaseFieldType):

	__slots__ = ["_PrcgPos", "_SctiesSttlmTxId"]
	@property
	def PrcgPos(self):
		return self._PrcgPos

	@PrcgPos.setter
	def PrcgPos(self, value):
		self._PrcgPos = value if value is not None else base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition9Choice, False)

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition9Choice, False)

	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxId', Max35Text, False)

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = base_types.UninitialisedField(self, 'SctiesSttlmTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))