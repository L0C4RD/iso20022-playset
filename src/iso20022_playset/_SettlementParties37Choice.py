# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveringPartiesAndAccount21
from . import ReceivingPartiesAndAccount21

class SettlementParties37Choice(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSttlmPties", "_RcvgSttlmPties"]
	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', DeliveringPartiesAndAccount21, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', DeliveringPartiesAndAccount21, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', ReceivingPartiesAndAccount21, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', ReceivingPartiesAndAccount21, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSttlmPties', type=DeliveringPartiesAndAccount21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=ReceivingPartiesAndAccount21, min=0, max=1, mutex_group=1, array=False),
	))