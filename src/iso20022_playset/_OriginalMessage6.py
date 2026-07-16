# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import Party50Choice

class OriginalMessage6(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlMsgNmId", "_OrgnlPackgId", "_OrgnlRcrdId", "_OrgnlSndr"]
	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

	@property
	def OrgnlPackgId(self):
		return self._OrgnlPackgId

	@OrgnlPackgId.setter
	def OrgnlPackgId(self, value):
		self._OrgnlPackgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPackgId', Max35Text, False)

	@OrgnlPackgId.deleter
	def OrgnlPackgId(self):
		del self._OrgnlPackgId
		self._OrgnlPackgId = base_types.UninitialisedField(self, 'OrgnlPackgId', Max35Text, False)

	@property
	def OrgnlRcrdId(self):
		return self._OrgnlRcrdId

	@OrgnlRcrdId.setter
	def OrgnlRcrdId(self, value):
		self._OrgnlRcrdId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRcrdId', Max35Text, False)

	@OrgnlRcrdId.deleter
	def OrgnlRcrdId(self):
		del self._OrgnlRcrdId
		self._OrgnlRcrdId = base_types.UninitialisedField(self, 'OrgnlRcrdId', Max35Text, False)

	@property
	def OrgnlSndr(self):
		return self._OrgnlSndr

	@OrgnlSndr.setter
	def OrgnlSndr(self, value):
		self._OrgnlSndr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlSndr', Party50Choice, False)

	@OrgnlSndr.deleter
	def OrgnlSndr(self):
		del self._OrgnlSndr
		self._OrgnlSndr = base_types.UninitialisedField(self, 'OrgnlSndr', Party50Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPackgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRcrdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
	))