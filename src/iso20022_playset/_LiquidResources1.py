# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LiquidResourceInformation1

class LiquidResources1(base_types._BaseFieldType):

	__slots__ = ["_CshDue", "_FcltiesCmmtdFxSwps", "_FcltiesCmmtdLinesOfCdt", "_FcltiesCmmtdRpAgrmts", "_FcltiesOthrCmmtd", "_FcltiesUcmmtd", "_FinInstrmsCCP", "_FinInstrmsDfltrsNonCshColl", "_FinInstrmsDfltrsSttlmColl", "_FinInstrmsTrsrInvstmts"]
	@property
	def CshDue(self):
		return self._CshDue

	@CshDue.setter
	def CshDue(self, value):
		self._CshDue = value if value is not None else base_types.UninitialisedField(self, 'CshDue', LiquidResourceInformation1, True)

	@CshDue.deleter
	def CshDue(self):
		del self._CshDue
		self._CshDue = base_types.UninitialisedField(self, 'CshDue', LiquidResourceInformation1, True)

	@property
	def FcltiesCmmtdFxSwps(self):
		return self._FcltiesCmmtdFxSwps

	@FcltiesCmmtdFxSwps.setter
	def FcltiesCmmtdFxSwps(self, value):
		self._FcltiesCmmtdFxSwps = value if value is not None else base_types.UninitialisedField(self, 'FcltiesCmmtdFxSwps', LiquidResourceInformation1, True)

	@FcltiesCmmtdFxSwps.deleter
	def FcltiesCmmtdFxSwps(self):
		del self._FcltiesCmmtdFxSwps
		self._FcltiesCmmtdFxSwps = base_types.UninitialisedField(self, 'FcltiesCmmtdFxSwps', LiquidResourceInformation1, True)

	@property
	def FcltiesCmmtdLinesOfCdt(self):
		return self._FcltiesCmmtdLinesOfCdt

	@FcltiesCmmtdLinesOfCdt.setter
	def FcltiesCmmtdLinesOfCdt(self, value):
		self._FcltiesCmmtdLinesOfCdt = value if value is not None else base_types.UninitialisedField(self, 'FcltiesCmmtdLinesOfCdt', LiquidResourceInformation1, True)

	@FcltiesCmmtdLinesOfCdt.deleter
	def FcltiesCmmtdLinesOfCdt(self):
		del self._FcltiesCmmtdLinesOfCdt
		self._FcltiesCmmtdLinesOfCdt = base_types.UninitialisedField(self, 'FcltiesCmmtdLinesOfCdt', LiquidResourceInformation1, True)

	@property
	def FcltiesCmmtdRpAgrmts(self):
		return self._FcltiesCmmtdRpAgrmts

	@FcltiesCmmtdRpAgrmts.setter
	def FcltiesCmmtdRpAgrmts(self, value):
		self._FcltiesCmmtdRpAgrmts = value if value is not None else base_types.UninitialisedField(self, 'FcltiesCmmtdRpAgrmts', LiquidResourceInformation1, True)

	@FcltiesCmmtdRpAgrmts.deleter
	def FcltiesCmmtdRpAgrmts(self):
		del self._FcltiesCmmtdRpAgrmts
		self._FcltiesCmmtdRpAgrmts = base_types.UninitialisedField(self, 'FcltiesCmmtdRpAgrmts', LiquidResourceInformation1, True)

	@property
	def FcltiesOthrCmmtd(self):
		return self._FcltiesOthrCmmtd

	@FcltiesOthrCmmtd.setter
	def FcltiesOthrCmmtd(self, value):
		self._FcltiesOthrCmmtd = value if value is not None else base_types.UninitialisedField(self, 'FcltiesOthrCmmtd', LiquidResourceInformation1, True)

	@FcltiesOthrCmmtd.deleter
	def FcltiesOthrCmmtd(self):
		del self._FcltiesOthrCmmtd
		self._FcltiesOthrCmmtd = base_types.UninitialisedField(self, 'FcltiesOthrCmmtd', LiquidResourceInformation1, True)

	@property
	def FcltiesUcmmtd(self):
		return self._FcltiesUcmmtd

	@FcltiesUcmmtd.setter
	def FcltiesUcmmtd(self, value):
		self._FcltiesUcmmtd = value if value is not None else base_types.UninitialisedField(self, 'FcltiesUcmmtd', LiquidResourceInformation1, True)

	@FcltiesUcmmtd.deleter
	def FcltiesUcmmtd(self):
		del self._FcltiesUcmmtd
		self._FcltiesUcmmtd = base_types.UninitialisedField(self, 'FcltiesUcmmtd', LiquidResourceInformation1, True)

	@property
	def FinInstrmsCCP(self):
		return self._FinInstrmsCCP

	@FinInstrmsCCP.setter
	def FinInstrmsCCP(self, value):
		self._FinInstrmsCCP = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmsCCP', LiquidResourceInformation1, True)

	@FinInstrmsCCP.deleter
	def FinInstrmsCCP(self):
		del self._FinInstrmsCCP
		self._FinInstrmsCCP = base_types.UninitialisedField(self, 'FinInstrmsCCP', LiquidResourceInformation1, True)

	@property
	def FinInstrmsDfltrsNonCshColl(self):
		return self._FinInstrmsDfltrsNonCshColl

	@FinInstrmsDfltrsNonCshColl.setter
	def FinInstrmsDfltrsNonCshColl(self, value):
		self._FinInstrmsDfltrsNonCshColl = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmsDfltrsNonCshColl', LiquidResourceInformation1, True)

	@FinInstrmsDfltrsNonCshColl.deleter
	def FinInstrmsDfltrsNonCshColl(self):
		del self._FinInstrmsDfltrsNonCshColl
		self._FinInstrmsDfltrsNonCshColl = base_types.UninitialisedField(self, 'FinInstrmsDfltrsNonCshColl', LiquidResourceInformation1, True)

	@property
	def FinInstrmsDfltrsSttlmColl(self):
		return self._FinInstrmsDfltrsSttlmColl

	@FinInstrmsDfltrsSttlmColl.setter
	def FinInstrmsDfltrsSttlmColl(self, value):
		self._FinInstrmsDfltrsSttlmColl = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmsDfltrsSttlmColl', LiquidResourceInformation1, True)

	@FinInstrmsDfltrsSttlmColl.deleter
	def FinInstrmsDfltrsSttlmColl(self):
		del self._FinInstrmsDfltrsSttlmColl
		self._FinInstrmsDfltrsSttlmColl = base_types.UninitialisedField(self, 'FinInstrmsDfltrsSttlmColl', LiquidResourceInformation1, True)

	@property
	def FinInstrmsTrsrInvstmts(self):
		return self._FinInstrmsTrsrInvstmts

	@FinInstrmsTrsrInvstmts.setter
	def FinInstrmsTrsrInvstmts(self, value):
		self._FinInstrmsTrsrInvstmts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmsTrsrInvstmts', LiquidResourceInformation1, True)

	@FinInstrmsTrsrInvstmts.deleter
	def FinInstrmsTrsrInvstmts(self):
		del self._FinInstrmsTrsrInvstmts
		self._FinInstrmsTrsrInvstmts = base_types.UninitialisedField(self, 'FinInstrmsTrsrInvstmts', LiquidResourceInformation1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshDue', type=LiquidResourceInformation1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdFxSwps', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdLinesOfCdt', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesCmmtdRpAgrmts', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesOthrCmmtd', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FcltiesUcmmtd', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsCCP', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsDfltrsNonCshColl', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsDfltrsSttlmColl', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmsTrsrInvstmts', type=LiquidResourceInformation1, min=0, max=None, mutex_group=None, array=True),
	))