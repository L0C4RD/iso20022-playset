# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class SettlementStatus27Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtlSttlm", "_Prtry", "_Sttld", "_Usttld"]
	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlm', ProprietaryReason4, True)

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = base_types.UninitialisedField(self, 'PrtlSttlm', ProprietaryReason4, True)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, True)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, True)

	@property
	def Usttld(self):
		return self._Usttld

	@Usttld.setter
	def Usttld(self, value):
		self._Usttld = value if value is not None else base_types.UninitialisedField(self, 'Usttld', ProprietaryReason4, True)

	@Usttld.deleter
	def Usttld(self):
		del self._Usttld
		self._Usttld = base_types.UninitialisedField(self, 'Usttld', ProprietaryReason4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlSttlm', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Usttld', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
	))