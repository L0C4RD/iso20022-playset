# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import PartyIdentification136
from . import SequenceRange1Choice

class ResendSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_BizDt", "_FileRef", "_OrgnlMsgNmId", "_Rcpt", "_SeqNb", "_SeqRg"]
	@property
	def BizDt(self):
		return self._BizDt

	@BizDt.setter
	def BizDt(self, value):
		self._BizDt = value if value is not None else base_types.UninitialisedField(self, 'BizDt', ISODate, False)

	@BizDt.deleter
	def BizDt(self):
		del self._BizDt
		self._BizDt = base_types.UninitialisedField(self, 'BizDt', ISODate, False)

	@property
	def FileRef(self):
		return self._FileRef

	@FileRef.setter
	def FileRef(self, value):
		self._FileRef = value if value is not None else base_types.UninitialisedField(self, 'FileRef', Max35Text, False)

	@FileRef.deleter
	def FileRef(self):
		del self._FileRef
		self._FileRef = base_types.UninitialisedField(self, 'FileRef', Max35Text, False)

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
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', PartyIdentification136, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', PartyIdentification136, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@property
	def SeqRg(self):
		return self._SeqRg

	@SeqRg.setter
	def SeqRg(self, value):
		self._SeqRg = value if value is not None else base_types.UninitialisedField(self, 'SeqRg', SequenceRange1Choice, False)

	@SeqRg.deleter
	def SeqRg(self):
		del self._SeqRg
		self._SeqRg = base_types.UninitialisedField(self, 'SeqRg', SequenceRange1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqRg', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
	))