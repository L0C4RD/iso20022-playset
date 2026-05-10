from . import base_types
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class CorporateActionNarrative35(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_NrrtvVrsn", "_TaxtnConds", "_PtyCtctNrrtv"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != base_types.auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if type(value) != base_types.auto else self.make_default("NrrtvVrsn")

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = None

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if type(value) != base_types.auto else self.make_default("PtyCtctNrrtv")

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = None

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if type(value) != base_types.auto else self.make_default("TaxtnConds")

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrrtvVrsn', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxtnConds', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
	))

