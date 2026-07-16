# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2
from . import SecurityIdentification14
from . import TotalVariationMargin1

class VariationMargin3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_FlsHrcut", "_MrkToMktFls", "_MrkToMktGrss", "_MrkToMktNetd", "_TtlMrkToMkt", "_TtlVartnMrgn"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@property
	def FlsHrcut(self):
		return self._FlsHrcut

	@FlsHrcut.setter
	def FlsHrcut(self, value):
		self._FlsHrcut = value if value is not None else base_types.UninitialisedField(self, 'FlsHrcut', Amount2, False)

	@FlsHrcut.deleter
	def FlsHrcut(self):
		del self._FlsHrcut
		self._FlsHrcut = base_types.UninitialisedField(self, 'FlsHrcut', Amount2, False)

	@property
	def MrkToMktFls(self):
		return self._MrkToMktFls

	@MrkToMktFls.setter
	def MrkToMktFls(self, value):
		self._MrkToMktFls = value if value is not None else base_types.UninitialisedField(self, 'MrkToMktFls', Amount2, True)

	@MrkToMktFls.deleter
	def MrkToMktFls(self):
		del self._MrkToMktFls
		self._MrkToMktFls = base_types.UninitialisedField(self, 'MrkToMktFls', Amount2, True)

	@property
	def MrkToMktGrss(self):
		return self._MrkToMktGrss

	@MrkToMktGrss.setter
	def MrkToMktGrss(self, value):
		self._MrkToMktGrss = value if value is not None else base_types.UninitialisedField(self, 'MrkToMktGrss', Amount2, True)

	@MrkToMktGrss.deleter
	def MrkToMktGrss(self):
		del self._MrkToMktGrss
		self._MrkToMktGrss = base_types.UninitialisedField(self, 'MrkToMktGrss', Amount2, True)

	@property
	def MrkToMktNetd(self):
		return self._MrkToMktNetd

	@MrkToMktNetd.setter
	def MrkToMktNetd(self, value):
		self._MrkToMktNetd = value if value is not None else base_types.UninitialisedField(self, 'MrkToMktNetd', Amount2, True)

	@MrkToMktNetd.deleter
	def MrkToMktNetd(self):
		del self._MrkToMktNetd
		self._MrkToMktNetd = base_types.UninitialisedField(self, 'MrkToMktNetd', Amount2, True)

	@property
	def TtlMrkToMkt(self):
		return self._TtlMrkToMkt

	@TtlMrkToMkt.setter
	def TtlMrkToMkt(self, value):
		self._TtlMrkToMkt = value if value is not None else base_types.UninitialisedField(self, 'TtlMrkToMkt', Amount2, False)

	@TtlMrkToMkt.deleter
	def TtlMrkToMkt(self):
		del self._TtlMrkToMkt
		self._TtlMrkToMkt = base_types.UninitialisedField(self, 'TtlMrkToMkt', Amount2, False)

	@property
	def TtlVartnMrgn(self):
		return self._TtlVartnMrgn

	@TtlVartnMrgn.setter
	def TtlVartnMrgn(self, value):
		self._TtlVartnMrgn = value if value is not None else base_types.UninitialisedField(self, 'TtlVartnMrgn', TotalVariationMargin1, True)

	@TtlVartnMrgn.deleter
	def TtlVartnMrgn(self):
		del self._TtlVartnMrgn
		self._TtlVartnMrgn = base_types.UninitialisedField(self, 'TtlVartnMrgn', TotalVariationMargin1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsHrcut', type=Amount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkToMktFls', type=Amount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrkToMktGrss', type=Amount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrkToMktNetd', type=Amount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlMrkToMkt', type=Amount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVartnMrgn', type=TotalVariationMargin1, min=1, max=None, mutex_group=None, array=True),
	))