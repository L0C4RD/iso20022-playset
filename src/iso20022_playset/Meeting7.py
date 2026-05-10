import base_types
import Max2048Text
import YesNoIndicator
import MeetingDateStatus2Code
import DateFormat58Choice
import QuorumQuantity2Choice
import LocationFormat1Choice

class Meeting7(base_types._BaseFieldType):

	__slots__ = ["_DtSts", "_QrmQty", "_URLAdr", "_DtAndTm", "_Lctn", "_QrmReqrd"]
	@property
	def DtSts(self):
		return self._DtSts

	@DtSts.setter
	def DtSts(self, value):
		self._DtSts = value if type(value) != auto else self.make_default("DtSts")

	@DtSts.deleter
	def DtSts(self):
		del self._DtSts
		self._DtSts = None

	@property
	def QrmQty(self):
		return self._QrmQty

	@QrmQty.setter
	def QrmQty(self, value):
		self._QrmQty = value if type(value) != auto else self.make_default("QrmQty")

	@QrmQty.deleter
	def QrmQty(self):
		del self._QrmQty
		self._QrmQty = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if type(value) != auto else self.make_default("DtAndTm")

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def QrmReqrd(self):
		return self._QrmReqrd

	@QrmReqrd.setter
	def QrmReqrd(self, value):
		self._QrmReqrd = value if type(value) != auto else self.make_default("QrmReqrd")

	@QrmReqrd.deleter
	def QrmReqrd(self):
		del self._QrmReqrd
		self._QrmReqrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtSts', type=MeetingDateStatus2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QrmQty', type=QuorumQuantity2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndTm', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=LocationFormat1Choice, min=1, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='QrmReqrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

