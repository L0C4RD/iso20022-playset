# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LinkedMessage6Choice
from . import Max350Text
from . import MessageRejectedReason2Code

class RejectionReason69(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_LkdMsg", "_Rsn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@property
	def LkdMsg(self):
		return self._LkdMsg

	@LkdMsg.setter
	def LkdMsg(self, value):
		self._LkdMsg = value if value is not None else base_types.UninitialisedField(self, 'LkdMsg', LinkedMessage6Choice, False)

	@LkdMsg.deleter
	def LkdMsg(self):
		del self._LkdMsg
		self._LkdMsg = base_types.UninitialisedField(self, 'LkdMsg', LinkedMessage6Choice, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', MessageRejectedReason2Code, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', MessageRejectedReason2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkdMsg', type=LinkedMessage6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=MessageRejectedReason2Code, min=1, max=1, mutex_group=None, array=False),
	))