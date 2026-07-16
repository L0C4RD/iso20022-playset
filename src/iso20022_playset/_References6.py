# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max70Text
from . import MessageIdentification1
from . import UseCases1Code

class References6(base_types._BaseFieldType):

	__slots__ = ["_AttchdDocNm", "_MsgId", "_PrcId", "_RjctdReqId", "_RjctdReqTp", "_RjctnRsn"]
	@property
	def AttchdDocNm(self):
		return self._AttchdDocNm

	@AttchdDocNm.setter
	def AttchdDocNm(self, value):
		self._AttchdDocNm = value if value is not None else base_types.UninitialisedField(self, 'AttchdDocNm', Max70Text, True)

	@AttchdDocNm.deleter
	def AttchdDocNm(self):
		del self._AttchdDocNm
		self._AttchdDocNm = base_types.UninitialisedField(self, 'AttchdDocNm', Max70Text, True)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def PrcId(self):
		return self._PrcId

	@PrcId.setter
	def PrcId(self, value):
		self._PrcId = value if value is not None else base_types.UninitialisedField(self, 'PrcId', MessageIdentification1, False)

	@PrcId.deleter
	def PrcId(self):
		del self._PrcId
		self._PrcId = base_types.UninitialisedField(self, 'PrcId', MessageIdentification1, False)

	@property
	def RjctdReqId(self):
		return self._RjctdReqId

	@RjctdReqId.setter
	def RjctdReqId(self, value):
		self._RjctdReqId = value if value is not None else base_types.UninitialisedField(self, 'RjctdReqId', MessageIdentification1, False)

	@RjctdReqId.deleter
	def RjctdReqId(self):
		del self._RjctdReqId
		self._RjctdReqId = base_types.UninitialisedField(self, 'RjctdReqId', MessageIdentification1, False)

	@property
	def RjctdReqTp(self):
		return self._RjctdReqTp

	@RjctdReqTp.setter
	def RjctdReqTp(self, value):
		self._RjctdReqTp = value if value is not None else base_types.UninitialisedField(self, 'RjctdReqTp', UseCases1Code, False)

	@RjctdReqTp.deleter
	def RjctdReqTp(self):
		del self._RjctdReqTp
		self._RjctdReqTp = base_types.UninitialisedField(self, 'RjctdReqTp', UseCases1Code, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', Max350Text, True)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', Max350Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdDocNm', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdReqTp', type=UseCases1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Max350Text, min=1, max=None, mutex_group=None, array=True),
	))