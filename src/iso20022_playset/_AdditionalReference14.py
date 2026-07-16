# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber5Choice
from . import Max35Text
from . import PartyIdentification247Choice

class AdditionalReference14(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_MsgNm", "_Ref", "_RefIssr"]
	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if value is not None else base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if value is not None else base_types.UninitialisedField(self, 'MsgNm', Max35Text, False)

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = base_types.UninitialisedField(self, 'MsgNm', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def RefIssr(self):
		return self._RefIssr

	@RefIssr.setter
	def RefIssr(self, value):
		self._RefIssr = value if value is not None else base_types.UninitialisedField(self, 'RefIssr', PartyIdentification247Choice, False)

	@RefIssr.deleter
	def RefIssr(self):
		del self._RefIssr
		self._RefIssr = base_types.UninitialisedField(self, 'RefIssr', PartyIdentification247Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefIssr', type=PartyIdentification247Choice, min=0, max=1, mutex_group=None, array=False),
	))