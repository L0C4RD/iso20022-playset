# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentType7Code
from . import GenericIdentification177
from . import Max35Text
from . import TrueFalseIndicator

class MessageStatusRequestData2(base_types._BaseFieldType):

	__slots__ = ["_DocQlfr", "_InitgPty", "_RctRprntFlg", "_XchgId"]
	@property
	def DocQlfr(self):
		return self._DocQlfr

	@DocQlfr.setter
	def DocQlfr(self, value):
		self._DocQlfr = value if value is not None else base_types.UninitialisedField(self, 'DocQlfr', DocumentType7Code, True)

	@DocQlfr.deleter
	def DocQlfr(self):
		del self._DocQlfr
		self._DocQlfr = base_types.UninitialisedField(self, 'DocQlfr', DocumentType7Code, True)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', GenericIdentification177, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', GenericIdentification177, False)

	@property
	def RctRprntFlg(self):
		return self._RctRprntFlg

	@RctRprntFlg.setter
	def RctRprntFlg(self, value):
		self._RctRprntFlg = value if value is not None else base_types.UninitialisedField(self, 'RctRprntFlg', TrueFalseIndicator, False)

	@RctRprntFlg.deleter
	def RctRprntFlg(self):
		del self._RctRprntFlg
		self._RctRprntFlg = base_types.UninitialisedField(self, 'RctRprntFlg', TrueFalseIndicator, False)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocQlfr', type=DocumentType7Code, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctRprntFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))