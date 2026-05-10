from . import base_types
import PartyIdentification139
import CountryCode
import ISODate
import FinancialInstrument71

class FundParameters5(base_types._BaseFieldType):

	__slots__ = ["_CtryOfDmcl", "_RegdDstrbtnCtry", "_FndMgmtCpny", "_DtFr", "_FinInstrmDtls"]
	@property
	def CtryOfDmcl(self):
		return self._CtryOfDmcl

	@CtryOfDmcl.setter
	def CtryOfDmcl(self, value):
		self._CtryOfDmcl = value if type(value) != auto else self.make_default("CtryOfDmcl")

	@CtryOfDmcl.deleter
	def CtryOfDmcl(self):
		del self._CtryOfDmcl
		self._CtryOfDmcl = None

	@property
	def RegdDstrbtnCtry(self):
		return self._RegdDstrbtnCtry

	@RegdDstrbtnCtry.setter
	def RegdDstrbtnCtry(self, value):
		self._RegdDstrbtnCtry = value if type(value) != auto else self.make_default("RegdDstrbtnCtry")

	@RegdDstrbtnCtry.deleter
	def RegdDstrbtnCtry(self):
		del self._RegdDstrbtnCtry
		self._RegdDstrbtnCtry = None

	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if type(value) != auto else self.make_default("FndMgmtCpny")

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = None

	@property
	def DtFr(self):
		return self._DtFr

	@DtFr.setter
	def DtFr(self, value):
		self._DtFr = value if type(value) != auto else self.make_default("DtFr")

	@DtFr.deleter
	def DtFr(self):
		del self._DtFr
		self._DtFr = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryOfDmcl', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdDstrbtnCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndMgmtCpny', type=PartyIdentification139, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument71, min=0, max=None, mutex_group=None, array=True),
	))

