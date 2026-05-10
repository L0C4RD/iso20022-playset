from . import base_types
from .ISODateTime import ISODateTime
from .Max140Text import Max140Text
from .Reconciliation3Code import Reconciliation3Code

class TechnicalAttributes5(base_types._BaseFieldType):

	__slots__ = ["_RptRctTmStmp", "_RcncltnFlg", "_TechRcrdId"]
	@property
	def RptRctTmStmp(self):
		return self._RptRctTmStmp

	@RptRctTmStmp.setter
	def RptRctTmStmp(self, value):
		self._RptRctTmStmp = value if type(value) != base_types.auto else self.make_default("RptRctTmStmp")

	@RptRctTmStmp.deleter
	def RptRctTmStmp(self):
		del self._RptRctTmStmp
		self._RptRctTmStmp = None

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if type(value) != base_types.auto else self.make_default("RcncltnFlg")

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptRctTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFlg', type=Reconciliation3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

