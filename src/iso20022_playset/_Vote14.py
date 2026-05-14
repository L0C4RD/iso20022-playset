# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._ProprietaryVote1 import ProprietaryVote1
from ._QuantityOrCode1Choice import QuantityOrCode1Choice

class Vote14(base_types._BaseFieldType):

	__slots__ = ["_Abstn", "_Agnst", "_AgnstMgmt", "_Blnk", "_Dscrtnry", "_For", "_IssrLabl", "_ListgGrpRsltnLabl", "_NoActn", "_OneYr", "_Prtry", "_ThreeYrs", "_TwoYrs", "_WthMgmt", "_Wthhld"]
	@property
	def Abstn(self):
		return self._Abstn

	@Abstn.setter
	def Abstn(self, value):
		self._Abstn = value if type(value) != base_types.auto else self.make_default("Abstn")

	@Abstn.deleter
	def Abstn(self):
		del self._Abstn
		self._Abstn = None

	@property
	def Agnst(self):
		return self._Agnst

	@Agnst.setter
	def Agnst(self, value):
		self._Agnst = value if type(value) != base_types.auto else self.make_default("Agnst")

	@Agnst.deleter
	def Agnst(self):
		del self._Agnst
		self._Agnst = None

	@property
	def AgnstMgmt(self):
		return self._AgnstMgmt

	@AgnstMgmt.setter
	def AgnstMgmt(self, value):
		self._AgnstMgmt = value if type(value) != base_types.auto else self.make_default("AgnstMgmt")

	@AgnstMgmt.deleter
	def AgnstMgmt(self):
		del self._AgnstMgmt
		self._AgnstMgmt = None

	@property
	def Blnk(self):
		return self._Blnk

	@Blnk.setter
	def Blnk(self, value):
		self._Blnk = value if type(value) != base_types.auto else self.make_default("Blnk")

	@Blnk.deleter
	def Blnk(self):
		del self._Blnk
		self._Blnk = None

	@property
	def Dscrtnry(self):
		return self._Dscrtnry

	@Dscrtnry.setter
	def Dscrtnry(self, value):
		self._Dscrtnry = value if type(value) != base_types.auto else self.make_default("Dscrtnry")

	@Dscrtnry.deleter
	def Dscrtnry(self):
		del self._Dscrtnry
		self._Dscrtnry = None

	@property
	def For(self):
		return self._For

	@For.setter
	def For(self, value):
		self._For = value if type(value) != base_types.auto else self.make_default("For")

	@For.deleter
	def For(self):
		del self._For
		self._For = None

	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if type(value) != base_types.auto else self.make_default("IssrLabl")

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = None

	@property
	def ListgGrpRsltnLabl(self):
		return self._ListgGrpRsltnLabl

	@ListgGrpRsltnLabl.setter
	def ListgGrpRsltnLabl(self, value):
		self._ListgGrpRsltnLabl = value if type(value) != base_types.auto else self.make_default("ListgGrpRsltnLabl")

	@ListgGrpRsltnLabl.deleter
	def ListgGrpRsltnLabl(self):
		del self._ListgGrpRsltnLabl
		self._ListgGrpRsltnLabl = None

	@property
	def NoActn(self):
		return self._NoActn

	@NoActn.setter
	def NoActn(self, value):
		self._NoActn = value if type(value) != base_types.auto else self.make_default("NoActn")

	@NoActn.deleter
	def NoActn(self):
		del self._NoActn
		self._NoActn = None

	@property
	def OneYr(self):
		return self._OneYr

	@OneYr.setter
	def OneYr(self, value):
		self._OneYr = value if type(value) != base_types.auto else self.make_default("OneYr")

	@OneYr.deleter
	def OneYr(self):
		del self._OneYr
		self._OneYr = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def ThreeYrs(self):
		return self._ThreeYrs

	@ThreeYrs.setter
	def ThreeYrs(self, value):
		self._ThreeYrs = value if type(value) != base_types.auto else self.make_default("ThreeYrs")

	@ThreeYrs.deleter
	def ThreeYrs(self):
		del self._ThreeYrs
		self._ThreeYrs = None

	@property
	def TwoYrs(self):
		return self._TwoYrs

	@TwoYrs.setter
	def TwoYrs(self, value):
		self._TwoYrs = value if type(value) != base_types.auto else self.make_default("TwoYrs")

	@TwoYrs.deleter
	def TwoYrs(self):
		del self._TwoYrs
		self._TwoYrs = None

	@property
	def WthMgmt(self):
		return self._WthMgmt

	@WthMgmt.setter
	def WthMgmt(self, value):
		self._WthMgmt = value if type(value) != base_types.auto else self.make_default("WthMgmt")

	@WthMgmt.deleter
	def WthMgmt(self):
		del self._WthMgmt
		self._WthMgmt = None

	@property
	def Wthhld(self):
		return self._Wthhld

	@Wthhld.setter
	def Wthhld(self, value):
		self._Wthhld = value if type(value) != base_types.auto else self.make_default("Wthhld")

	@Wthhld.deleter
	def Wthhld(self):
		del self._Wthhld
		self._Wthhld = None

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