# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ProprietaryVote1
from . import QuantityOrCode1Choice

class Vote21(base_types._BaseFieldType):

	__slots__ = ["_Abstn", "_Agnst", "_AgnstMgmt", "_Blnk", "_Dscrtnry", "_For", "_IssrLabl", "_ListgGrpRsltnLabl", "_NoActn", "_OneYr", "_Prtry", "_ThreeYrs", "_TwoYrs", "_WthMgmt", "_Wthhld"]
	@property
	def Abstn(self):
		return self._Abstn

	@Abstn.setter
	def Abstn(self, value):
		self._Abstn = value if value is not None else base_types.UninitialisedField(self, 'Abstn', QuantityOrCode1Choice, False)

	@Abstn.deleter
	def Abstn(self):
		del self._Abstn
		self._Abstn = base_types.UninitialisedField(self, 'Abstn', QuantityOrCode1Choice, False)

	@property
	def Agnst(self):
		return self._Agnst

	@Agnst.setter
	def Agnst(self, value):
		self._Agnst = value if value is not None else base_types.UninitialisedField(self, 'Agnst', QuantityOrCode1Choice, False)

	@Agnst.deleter
	def Agnst(self):
		del self._Agnst
		self._Agnst = base_types.UninitialisedField(self, 'Agnst', QuantityOrCode1Choice, False)

	@property
	def AgnstMgmt(self):
		return self._AgnstMgmt

	@AgnstMgmt.setter
	def AgnstMgmt(self, value):
		self._AgnstMgmt = value if value is not None else base_types.UninitialisedField(self, 'AgnstMgmt', QuantityOrCode1Choice, False)

	@AgnstMgmt.deleter
	def AgnstMgmt(self):
		del self._AgnstMgmt
		self._AgnstMgmt = base_types.UninitialisedField(self, 'AgnstMgmt', QuantityOrCode1Choice, False)

	@property
	def Blnk(self):
		return self._Blnk

	@Blnk.setter
	def Blnk(self, value):
		self._Blnk = value if value is not None else base_types.UninitialisedField(self, 'Blnk', QuantityOrCode1Choice, False)

	@Blnk.deleter
	def Blnk(self):
		del self._Blnk
		self._Blnk = base_types.UninitialisedField(self, 'Blnk', QuantityOrCode1Choice, False)

	@property
	def Dscrtnry(self):
		return self._Dscrtnry

	@Dscrtnry.setter
	def Dscrtnry(self, value):
		self._Dscrtnry = value if value is not None else base_types.UninitialisedField(self, 'Dscrtnry', QuantityOrCode1Choice, False)

	@Dscrtnry.deleter
	def Dscrtnry(self):
		del self._Dscrtnry
		self._Dscrtnry = base_types.UninitialisedField(self, 'Dscrtnry', QuantityOrCode1Choice, False)

	@property
	def For(self):
		return self._For

	@For.setter
	def For(self, value):
		self._For = value if value is not None else base_types.UninitialisedField(self, 'For', QuantityOrCode1Choice, False)

	@For.deleter
	def For(self):
		del self._For
		self._For = base_types.UninitialisedField(self, 'For', QuantityOrCode1Choice, False)

	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if value is not None else base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@property
	def ListgGrpRsltnLabl(self):
		return self._ListgGrpRsltnLabl

	@ListgGrpRsltnLabl.setter
	def ListgGrpRsltnLabl(self, value):
		self._ListgGrpRsltnLabl = value if value is not None else base_types.UninitialisedField(self, 'ListgGrpRsltnLabl', Max35Text, False)

	@ListgGrpRsltnLabl.deleter
	def ListgGrpRsltnLabl(self):
		del self._ListgGrpRsltnLabl
		self._ListgGrpRsltnLabl = base_types.UninitialisedField(self, 'ListgGrpRsltnLabl', Max35Text, False)

	@property
	def NoActn(self):
		return self._NoActn

	@NoActn.setter
	def NoActn(self, value):
		self._NoActn = value if value is not None else base_types.UninitialisedField(self, 'NoActn', QuantityOrCode1Choice, False)

	@NoActn.deleter
	def NoActn(self):
		del self._NoActn
		self._NoActn = base_types.UninitialisedField(self, 'NoActn', QuantityOrCode1Choice, False)

	@property
	def OneYr(self):
		return self._OneYr

	@OneYr.setter
	def OneYr(self, value):
		self._OneYr = value if value is not None else base_types.UninitialisedField(self, 'OneYr', QuantityOrCode1Choice, False)

	@OneYr.deleter
	def OneYr(self):
		del self._OneYr
		self._OneYr = base_types.UninitialisedField(self, 'OneYr', QuantityOrCode1Choice, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryVote1, True)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryVote1, True)

	@property
	def ThreeYrs(self):
		return self._ThreeYrs

	@ThreeYrs.setter
	def ThreeYrs(self, value):
		self._ThreeYrs = value if value is not None else base_types.UninitialisedField(self, 'ThreeYrs', QuantityOrCode1Choice, False)

	@ThreeYrs.deleter
	def ThreeYrs(self):
		del self._ThreeYrs
		self._ThreeYrs = base_types.UninitialisedField(self, 'ThreeYrs', QuantityOrCode1Choice, False)

	@property
	def TwoYrs(self):
		return self._TwoYrs

	@TwoYrs.setter
	def TwoYrs(self, value):
		self._TwoYrs = value if value is not None else base_types.UninitialisedField(self, 'TwoYrs', QuantityOrCode1Choice, False)

	@TwoYrs.deleter
	def TwoYrs(self):
		del self._TwoYrs
		self._TwoYrs = base_types.UninitialisedField(self, 'TwoYrs', QuantityOrCode1Choice, False)

	@property
	def WthMgmt(self):
		return self._WthMgmt

	@WthMgmt.setter
	def WthMgmt(self, value):
		self._WthMgmt = value if value is not None else base_types.UninitialisedField(self, 'WthMgmt', QuantityOrCode1Choice, False)

	@WthMgmt.deleter
	def WthMgmt(self):
		del self._WthMgmt
		self._WthMgmt = base_types.UninitialisedField(self, 'WthMgmt', QuantityOrCode1Choice, False)

	@property
	def Wthhld(self):
		return self._Wthhld

	@Wthhld.setter
	def Wthhld(self, value):
		self._Wthhld = value if value is not None else base_types.UninitialisedField(self, 'Wthhld', QuantityOrCode1Choice, False)

	@Wthhld.deleter
	def Wthhld(self):
		del self._Wthhld
		self._Wthhld = base_types.UninitialisedField(self, 'Wthhld', QuantityOrCode1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Abstn', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agnst', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgnstMgmt', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Blnk', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscrtnry', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='For', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListgGrpRsltnLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoActn', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OneYr', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryVote1, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='ThreeYrs', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwoYrs', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WthMgmt', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wthhld', type=QuantityOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
	))