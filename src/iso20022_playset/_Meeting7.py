# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat58Choice
from . import LocationFormat1Choice
from . import Max2048Text
from . import MeetingDateStatus2Code
from . import QuorumQuantity2Choice
from . import YesNoIndicator

class Meeting7(base_types._BaseFieldType):

	__slots__ = ["_DtAndTm", "_DtSts", "_Lctn", "_QrmQty", "_QrmReqrd", "_URLAdr"]
	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if value is not None else base_types.UninitialisedField(self, 'DtAndTm', DateFormat58Choice, False)

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = base_types.UninitialisedField(self, 'DtAndTm', DateFormat58Choice, False)

	@property
	def DtSts(self):
		return self._DtSts

	@DtSts.setter
	def DtSts(self, value):
		self._DtSts = value if value is not None else base_types.UninitialisedField(self, 'DtSts', MeetingDateStatus2Code, False)

	@DtSts.deleter
	def DtSts(self):
		del self._DtSts
		self._DtSts = base_types.UninitialisedField(self, 'DtSts', MeetingDateStatus2Code, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', LocationFormat1Choice, True)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', LocationFormat1Choice, True)

	@property
	def QrmQty(self):
		return self._QrmQty

	@QrmQty.setter
	def QrmQty(self, value):
		self._QrmQty = value if value is not None else base_types.UninitialisedField(self, 'QrmQty', QuorumQuantity2Choice, False)

	@QrmQty.deleter
	def QrmQty(self):
		del self._QrmQty
		self._QrmQty = base_types.UninitialisedField(self, 'QrmQty', QuorumQuantity2Choice, False)

	@property
	def QrmReqrd(self):
		return self._QrmReqrd

	@QrmReqrd.setter
	def QrmReqrd(self, value):
		self._QrmReqrd = value if value is not None else base_types.UninitialisedField(self, 'QrmReqrd', YesNoIndicator, False)

	@QrmReqrd.deleter
	def QrmReqrd(self):
		del self._QrmReqrd
		self._QrmReqrd = base_types.UninitialisedField(self, 'QrmReqrd', YesNoIndicator, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndTm', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtSts', type=MeetingDateStatus2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=LocationFormat1Choice, min=1, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='QrmQty', type=QuorumQuantity2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QrmReqrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))