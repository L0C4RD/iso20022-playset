from . import base_types
from ._TotalVariationMargin1 import TotalVariationMargin1
from ._Amount2 import Amount2
from ._SecurityIdentification14 import SecurityIdentification14

class VariationMargin3(base_types._BaseFieldType):

	__slots__ = ["_FlsHrcut", "_MrkToMktGrss", "_MrkToMktNetd", "_FinInstrmId", "_TtlVartnMrgn", "_TtlMrkToMkt", "_MrkToMktFls"]
	@property
	def FlsHrcut(self):
		return self._FlsHrcut

	@FlsHrcut.setter
	def FlsHrcut(self, value):
		self._FlsHrcut = value if type(value) != base_types.auto else self.make_default("FlsHrcut")

	@FlsHrcut.deleter
	def FlsHrcut(self):
		del self._FlsHrcut
		self._FlsHrcut = None

	@property
	def MrkToMktGrss(self):
		return self._MrkToMktGrss

	@MrkToMktGrss.setter
	def MrkToMktGrss(self, value):
		self._MrkToMktGrss = value if type(value) != base_types.auto else self.make_default("MrkToMktGrss")

	@MrkToMktGrss.deleter
	def MrkToMktGrss(self):
		del self._MrkToMktGrss
		self._MrkToMktGrss = None

	@property
	def MrkToMktNetd(self):
		return self._MrkToMktNetd

	@MrkToMktNetd.setter
	def MrkToMktNetd(self, value):
		self._MrkToMktNetd = value if type(value) != base_types.auto else self.make_default("MrkToMktNetd")

	@MrkToMktNetd.deleter
	def MrkToMktNetd(self):
		del self._MrkToMktNetd
		self._MrkToMktNetd = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def TtlVartnMrgn(self):
		return self._TtlVartnMrgn

	@TtlVartnMrgn.setter
	def TtlVartnMrgn(self, value):
		self._TtlVartnMrgn = value if type(value) != base_types.auto else self.make_default("TtlVartnMrgn")

	@TtlVartnMrgn.deleter
	def TtlVartnMrgn(self):
		del self._TtlVartnMrgn
		self._TtlVartnMrgn = None

	@property
	def TtlMrkToMkt(self):
		return self._TtlMrkToMkt

	@TtlMrkToMkt.setter
	def TtlMrkToMkt(self, value):
		self._TtlMrkToMkt = value if type(value) != base_types.auto else self.make_default("TtlMrkToMkt")

	@TtlMrkToMkt.deleter
	def TtlMrkToMkt(self):
		del self._TtlMrkToMkt
		self._TtlMrkToMkt = None

	@property
	def MrkToMktFls(self):
		return self._MrkToMktFls

	@MrkToMktFls.setter
	def MrkToMktFls(self, value):
		self._MrkToMktFls = value if type(value) != base_types.auto else self.make_default("MrkToMktFls")

	@MrkToMktFls.deleter
	def MrkToMktFls(self):
		del self._MrkToMktFls
		self._MrkToMktFls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FlsHrcut', type=Amount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkToMktGrss', type=Amount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrkToMktNetd', type=Amount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVartnMrgn', type=TotalVariationMargin1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlMrkToMkt', type=Amount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkToMktFls', type=Amount2, min=0, max=None, mutex_group=None, array=True),
	))

