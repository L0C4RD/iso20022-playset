from . import base_types
from .LiquidResourceInformation1 import LiquidResourceInformation1

class LiquidResources1(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmsTrsrInvstmts", "_FinInstrmsDfltrsSttlmColl", "_FcltiesCmmtdRpAgrmts", "_FinInstrmsDfltrsNonCshColl", "_FcltiesOthrCmmtd", "_FcltiesUcmmtd", "_CshDue", "_FcltiesCmmtdFxSwps", "_FcltiesCmmtdLinesOfCdt", "_FinInstrmsCCP"]
	@property
	def FinInstrmsTrsrInvstmts(self):
		return self._FinInstrmsTrsrInvstmts

	@FinInstrmsTrsrInvstmts.setter
	def FinInstrmsTrsrInvstmts(self, value):
		self._FinInstrmsTrsrInvstmts = value if type(value) != base_types.auto else self.make_default("FinInstrmsTrsrInvstmts")

	@FinInstrmsTrsrInvstmts.deleter
	def FinInstrmsTrsrInvstmts(self):
		del self._FinInstrmsTrsrInvstmts
		self._FinInstrmsTrsrInvstmts = None

	@property
	def FinInstrmsDfltrsSttlmColl(self):
		return self._FinInstrmsDfltrsSttlmColl

	@FinInstrmsDfltrsSttlmColl.setter
	def FinInstrmsDfltrsSttlmColl(self, value):
		self._FinInstrmsDfltrsSttlmColl = value if type(value) != base_types.auto else self.make_default("FinInstrmsDfltrsSttlmColl")

	@FinInstrmsDfltrsSttlmColl.deleter
	def FinInstrmsDfltrsSttlmColl(self):
		del self._FinInstrmsDfltrsSttlmColl
		self._FinInstrmsDfltrsSttlmColl = None

	@property
	def FcltiesCmmtdRpAgrmts(self):
		return self._FcltiesCmmtdRpAgrmts

	@FcltiesCmmtdRpAgrmts.setter
	def FcltiesCmmtdRpAgrmts(self, value):
		self._FcltiesCmmtdRpAgrmts = value if type(value) != base_types.auto else self.make_default("FcltiesCmmtdRpAgrmts")

	@FcltiesCmmtdRpAgrmts.deleter
	def FcltiesCmmtdRpAgrmts(self):
		del self._FcltiesCmmtdRpAgrmts
		self._FcltiesCmmtdRpAgrmts = None

	@property
	def FinInstrmsDfltrsNonCshColl(self):
		return self._FinInstrmsDfltrsNonCshColl

	@FinInstrmsDfltrsNonCshColl.setter
	def FinInstrmsDfltrsNonCshColl(self, value):
		self._FinInstrmsDfltrsNonCshColl = value if type(value) != base_types.auto else self.make_default("FinInstrmsDfltrsNonCshColl")

	@FinInstrmsDfltrsNonCshColl.deleter
	def FinInstrmsDfltrsNonCshColl(self):
		del self._FinInstrmsDfltrsNonCshColl
		self._FinInstrmsDfltrsNonCshColl = None

	@property
	def FcltiesOthrCmmtd(self):
		return self._FcltiesOthrCmmtd

	@FcltiesOthrCmmtd.setter
	def FcltiesOthrCmmtd(self, value):
		self._FcltiesOthrCmmtd = value if type(value) != base_types.auto else self.make_default("FcltiesOthrCmmtd")

	@FcltiesOthrCmmtd.deleter
	def FcltiesOthrCmmtd(self):
		del self._FcltiesOthrCmmtd
		self._FcltiesOthrCmmtd = None

	@property
	def FcltiesUcmmtd(self):
		return self._FcltiesUcmmtd

	@FcltiesUcmmtd.setter
	def FcltiesUcmmtd(self, value):
		self._FcltiesUcmmtd = value if type(value) != base_types.auto else self.make_default("FcltiesUcmmtd")

	@FcltiesUcmmtd.deleter
	def FcltiesUcmmtd(self):
		del self._FcltiesUcmmtd
		self._FcltiesUcmmtd = None

	@property
	def CshDue(self):
		return self._CshDue

	@CshDue.setter
	def CshDue(self, value):
		self._CshDue = value if type(value) != base_types.auto else self.make_default("CshDue")

	@CshDue.deleter
	def CshDue(self):
		del self._CshDue
		self._CshDue = None

	@property
	def FcltiesCmmtdFxSwps(self):
		return self._FcltiesCmmtdFxSwps

	@FcltiesCmmtdFxSwps.setter
	def FcltiesCmmtdFxSwps(self, value):
		self._FcltiesCmmtdFxSwps = value if type(value) != base_types.auto else self.make_default("FcltiesCmmtdFxSwps")

	@FcltiesCmmtdFxSwps.deleter
	def FcltiesCmmtdFxSwps(self):
		del self._FcltiesCmmtdFxSwps
		self._FcltiesCmmtdFxSwps = None

	@property
	def FcltiesCmmtdLinesOfCdt(self):
		return self._FcltiesCmmtdLinesOfCdt

	@FcltiesCmmtdLinesOfCdt.setter
	def FcltiesCmmtdLinesOfCdt(self, value):
		self._FcltiesCmmtdLinesOfCdt = value if type(value) != base_types.auto else self.make_default("FcltiesCmmtdLinesOfCdt")

	@FcltiesCmmtdLinesOfCdt.deleter
	def FcltiesCmmtdLinesOfCdt(self):
		del self._FcltiesCmmtdLinesOfCdt
		self._FcltiesCmmtdLinesOfCdt = None

	@property
	def FinInstrmsCCP(self):
		return self._FinInstrmsCCP

	@FinInstrmsCCP.setter
	def FinInstrmsCCP(self, value):
		self._FinInstrmsCCP = value if type(value) != base_types.auto else self.make_default("FinInstrmsCCP")

	@FinInstrmsCCP.deleter
	def FinInstrmsCCP(self):
		del self._FinInstrmsCCP
		self._FinInstrmsCCP = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmsTrsrInvstmts', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsDfltrsSttlmColl', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdRpAgrmts', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsDfltrsNonCshColl', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesOthrCmmtd', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesUcmmtd', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshDue', type=LiquidResourceInformation1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdFxSwps', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdLinesOfCdt', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsCCP', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
	))

